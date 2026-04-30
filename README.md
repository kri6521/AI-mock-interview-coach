# AI-mock-interview-coach

## 🚀 Setup Instructions

```bash
git clone <repo_url>
cd AI-mock-interview-coach

pip install -r requirements.txt
```
### Add your API key
```
Groq(api_key="YOUR_API_KEY")
```
### Run the app
```
streamlit run app.py
```

## 🧠 Architecture Overview

This system uses a **multi-agent architecture** consisting of three main components:

---

### 1. 🎤 Interviewer Agent

The Interviewer Agent is responsible for generating and managing interview questions.

**Key Features:**
- Generates questions dynamically
- Adapts difficulty based on user performance

**Modes:**
- `normal` – Standard question flow
- `followup` – Asks deeper questions based on previous answers
- `increase_difficulty` – Raises complexity as performance improves

---

### 2. 📊 Evaluator Agent

The Evaluator Agent analyzes and scores the user's responses.

**Evaluation Criteria:**
- Clarity  
- Depth  
- Correctness  
- Communication  

**Capabilities:**
- Outputs structured JSON responses
- Determines whether a follow-up question is required

---

### 3. 🧑‍🏫 Coach Agent

The Coach Agent provides actionable feedback to help users improve.

**Provides:**
- Strengths  
- Weaknesses  
- Areas of improvement  
- Personalized **7-day improvement plan**

---
