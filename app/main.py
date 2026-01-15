import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from datetime import datetime, timezone

# LangChain Imports
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Import our models
from app.models import ReviewSubmission

# 1. Setup & Config
load_dotenv()
app = FastAPI()

# Setup Templates (Points to your 'app/templates' folder)
templates = Jinja2Templates(directory="app/templates")

# 2. Database Connection (MongoDB)
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["fynd_assessment"]  # The database name
collection = db["reviews"]      # The collection (like a table)

# 3. AI Setup (Groq)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
parser = JsonOutputParser()

# 4. The Prompt Logic
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """
    You are a customer experience AI for an e-commerce platform.
    Match your tone to the rating:
    1-2 stars: apologetic and corrective
    3 stars: neutral and improvement-focused
    4-5 stars: appreciative and loyalty-building
    Return valid JSON only.
    """),
    ("user", """
    Analyze this review:
    Rating: {rating} stars
    Text: {review}

    Return a JSON object with exactly these 3 keys:
    1. "ai_response": A polite reply to the customer.
    2. "ai_summary": A 1-sentence summary for the admin.
    3. "recommended_actions": A short list of actions for the internal team.

    {format_instructions}
    """)
])
chain = prompt_template | llm | parser

# --- ROUTES ---

# Route 1: Serve the User Dashboard (HTML)
@app.get("/", response_class=HTMLResponse)
async def read_user_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route 2: Serve the Admin Dashboard (HTML)
@app.get("/admin", response_class=HTMLResponse)
async def read_admin_dashboard(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# Route 3: Handle Review Submission (API)
@app.post("/submit-review")
async def submit_review(submission: ReviewSubmission):
    try:
        # INPUT VALIDATION
        if not submission.review.strip():
            raise HTTPException(
                status_code=400,
                detail="Review cannot be empty"
            )

        # A. Get AI analysis
        ai_output = chain.invoke({
            "rating": submission.rating, 
            "review": submission.review,
            "format_instructions": parser.get_format_instructions()
        })

        # B. Prepare document for MongoDB
        doc = {
            "user_rating": submission.rating,
            "user_review": submission.review,
            "ai_response": ai_output.get("ai_response"),
            "ai_summary": ai_output.get("ai_summary"),
            "recommended_actions": ai_output.get("recommended_actions"),
            "created_at": datetime.now(timezone.utc)
        }

        # C. Insert into DB
        collection.insert_one(doc)

        return {"ai_response": ai_output.get("ai_response")}
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Route 4: Get All Reviews for Admin (API)
@app.get("/api/reviews")
async def get_reviews():
    # Fetch all reviews, exclude the Mongo ID object (it causes issues with JSON)
    reviews = list(collection.find({}, {"_id": 0}).sort("_id", -1))
    return reviews