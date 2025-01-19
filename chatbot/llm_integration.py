import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_response(query, context):
    prompt = f"""You are a chatbot that answers based on the following context:
    {context}
    Query: {query}
    Response:"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=200
    )
    return response['choices'][0]['message']['content']
