# 🤖 ReviewSense AI: The Feedback Loop That Never Sleeps

> **"What if your customer service rep was awake 24/7, read every review in milliseconds, and never got tired of saying sorry for cold pizza?"**

**ReviewSense AI** is a production-ready sentiment analysis pipeline that automates the chaotic world of customer feedback. It doesn't just read reviews; it *understands* them, rates them, and tells management exactly how to fix the problem—all in real-time.

---

## 🏆 Project Highlights

This system was engineered to solve real operational bottlenecks, focusing on reliability and structured data.

* **⚡ High-Performance Pipeline:** Built an evaluation and inference engine using **FastAPI** and **Groq (LLaMA-3.1-8B-Instant)** capable of handling burst traffic while enforcing strict schema-safe outputs.
* **🎯 73% Accuracy Benchmark:** Rigorously evaluated 3 prompt engineering strategies (Zero-shot, Few-shot, Criteria-based) on **122 real-world Yelp reviews**, achieving consistently higher accuracy than baseline models.
* **🛡️ 100% JSON Validity:** Implemented a robust parsing layer using **LangChain** that guarantees structured data outputs, eliminating hallucinated formats.
* **📊 Live Operational Dashboard:** Deployed a dual-interface web app on **Render** backed by **MongoDB Atlas**, enabling real-time AI responses for users and actionable analytics for admins.

---

## 🕹️ How It Works

The system operates on a stateless inference architecture with persistent storage.

### 1. The User Experience (Frontend)
A customer drops a review (e.g., *"The soup was cold but the server was nice"*).
* **Action:** The backend processes the text via the Groq API.
* **Result:** The user gets an *instant*, empathetic, AI-generated reply acknowledging their specific issue.

### 2. The Brain (Backend & AI)
Instead of generic sentiment analysis, the system uses **Criteria-Based Prompting** to analyze:
1.  **Polarity:** Is this positive or negative?
2.  **Intensity:** How angry/happy are they?
3.  **Specifics:** What went wrong? (Service, Food, Ambiance)

### 3. The Admin Intelligence (Dashboard)
Managers don't have time to read 1,000 essays. The dashboard shows:
* **One-Sentence Summaries:** *"Customer upset about wait times, praised the garlic bread."*
* **Actionable Advice:** *"Investigate kitchen delays during Tuesday lunch rush."*

---

## 🧪 The "Science" Behind It (Task 1)

I conducted a scientific evaluation to determine the optimal prompting strategy for this use case.

| Strategy | Accuracy | Latency | Verdict |
| :--- | :--- | :--- | :--- |
| **Zero-Shot** | 65% | ⚡ Fastest | Good for simple tasks, struggled with sarcasm. |
| **Few-Shot** | 71% | 🐢 Slower | Better, but got confused by mixed reviews. |
| **Criteria-Based** | **73%** | ⚖️ Balanced | **The Winner.** Reasoning step anchors the model before prediction. |

*Check out the [Notebook](./notebooks/EvaluateStratergy.ipynb) for the full breakdown.*

---

## 🛠️ Tech Stack

* **Brain:** LLaMA-3.1-8B-Instant (via Groq API) - *Chosen for sub-second latency.*
* **Backbone:** Python, FastAPI, Uvicorn - *Async prowess for handling concurrent requests.*
* **Orchestration:** LangChain - *For managing prompt templates and chains.*
* **Memory:** MongoDB Atlas - *Cloud-native NoSQL storage.*
* **Face:** HTML5, CSS3, Vanilla JS - *Lightweight, dependency-free frontend.*
* **Home:** Render - *CI/CD auto-deployment.*

---

## 🚀 Run It Locally

Want to see it in action?

### 1. Clone the repo

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ReviewSense-AI.git
cd ReviewSense-AI

2. Install dependencies
Bash

pip install -r requirements.txt
3. Set up your secrets
Create a .env file in the root directory:

Code snippet

GROQ_API_KEY=gsk_your_key_here
MONGO_URI=mongodb+srv://your_mongo_url
4. Launch!
Bash

uvicorn app.main:app --reload
User View: Visit http://localhost:8000

Admin View: Visit http://localhost:8000/admin

```
---
🔗 Live App: https://fynd-ai-intern-5moe.onrender.com
🔗 Admin Dashboard: https://fynd-ai-intern-5moe.onrender.com/admin
---

🔮 Future Roadmap
[ ] Sentiment Trend Analysis: Visual graphs showing if customers are getting happier over time.

[ ] Authentication: Adding JWT auth so customers can't see the Admin panel.

[ ] Slack Integration: Pinging the "Kitchen Team" channel automatically when a 1-star review drops.

Built with ☕ and 🐍 by Pratik.

Contact
Feel free to connect with me on LinkedIn to discuss this project or other data opportunities:

[https://www.linkedin.com/in/pratik-kishor/]
