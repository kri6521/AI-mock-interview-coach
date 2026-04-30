from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def load_prompt():
    with open("prompts/coach.txt", "r") as f:
        return f.read()

def coach_agent(history, evaluations):
    template = load_prompt()

    prompt = template.format(
        history=history,
        evaluations=evaluations
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content
