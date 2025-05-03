import openai

def generate_company_summary(data):
    prompt = f"Summarize the following company data in a professional tone:\n{data}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
