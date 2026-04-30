from groq import Groq
import json

client = Groq(api_key="YOUR_API_KEY")

def load_prompt():
    with open("prompts/evaluator.txt", "r") as f:
        return f.read()

def evaluator_agent(answer):
    template = load_prompt()
    prompt = template.format(answer=answer)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": prompt}]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {
            "clarity": 5,
            "depth": 5,
            "correctness": 5,
            "communication": 5,
            "strengths": ["Average answer"],
            "weaknesses": ["Needs improvement"],
            "followup_needed": False
        }
