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

### 1. Interviewer Agent

The Interviewer Agent is responsible for generating and managing interview questions.

**Key Features:**
- Generates questions dynamically
- Adapts difficulty based on user performance

**Modes:**
- `normal` – Standard question flow
- `followup` – Asks deeper questions based on previous answers
- `increase_difficulty` – Raises complexity as performance improves

---

### 2. Evaluator Agent

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

### 3. Coach Agent

The Coach Agent provides actionable feedback to help users improve.

**Provides:**
- Strengths  
- Weaknesses  
- Areas of improvement  
- Personalized **7-day improvement plan**

---

### 4. Orchestrator

Controls flow using:
```
decide_mode()
```
- Adapts interview difficulty dynamically

---

## ⚙️ Key Design Decisions

This system is built with thoughtful design choices to ensure flexibility, scalability, and ease of development.

---

### 1. Prompt Separation

Prompts are stored in the `/prompts` directory.

**Benefits:**
- Easy to iterate and refine prompts
- No need to modify core application code
- Enables faster experimentation

---

### 2. JSON Evaluation

The Evaluator Agent outputs responses in structured JSON format.

**Enables:**
- Consistent scoring mechanism  
- Adaptive interview logic  
- Easy integration with analytics pipelines  

---

### 3. Multi-Agent Design

The system uses multiple specialized agents instead of a single LLM.

**Advantages:**
- Better modularity  
- Clear separation of responsibilities  
- Easier debugging and scaling  

---

### 4. Trade-offs

| Decision            | Trade-off                                      |
|--------------------|-----------------------------------------------|
| Separate agents    | + Modular design, − More API calls            |
| LLM evaluation     | + Flexible evaluation, − Possible inconsistency |
| Streamlit UI       | + Fast prototyping, − Limited scalability     |

---

## 🧪 Example Interview Transcripts

Below are sample interactions demonstrating how the system evaluates different types of candidates.

---

### ✅ Strong Candidate

**Q:** Explain overfitting  
**A:** Overfitting occurs when a model learns noise instead of pattern...

**Evaluation:**
- Clarity: 9  
- Depth: 8  
- Correctness: 9  

➡ **Next Step:**  
- Increase difficulty  
- Next question focuses on **regularization techniques**

---

### ❌ Weak Candidate

**Q:** What is a hash map?  
**A:** It stores data  

**Evaluation:**
- Clarity: 3  
- Depth: 2  

➡ **Next Step:**  
- Ask a follow-up question  

**Follow-up:**  
> Can you explain how keys are mapped to values?

---

### ⚠️ Edge Case (Hallucination)

**Q:** Explain gradient descent  
**A:** It increases loss to find maximum  

**Evaluation:**
- Correctness: 1  

➡ **Next Step:**  
- Ask a corrective follow-up question  
- Coach highlights conceptual misunderstanding  

---
