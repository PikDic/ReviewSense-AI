from pydantic import BaseModel
from typing import Optional

# Model for the data coming FROM the user (User Dashboard)
class ReviewSubmission(BaseModel):
    rating: int
    review: str

# Model for the data going TO the database (Admin Dashboard)
# We don't strictly need this for Mongo, but it helps document what we are storing.
class ReviewRecord(BaseModel):
    user_rating: int
    user_review: str
    ai_response: str
    ai_summary: str
    recommended_actions: str