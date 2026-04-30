from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def load_prompt():
    with open("prompts/interviewer.txt", "r") as f:
        return f.read()

def interviewer_agent(role, focus, history, evaluation_summary, mode):
    template = load_prompt()

    prompt = template.format(
        role=role,
        focus=focus,
        history=history,
        evaluation_summary=evaluation_summary,
        mode=mode
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
