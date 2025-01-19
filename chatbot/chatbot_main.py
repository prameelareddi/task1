from vector_search import search_knowledge_base
from llm_integration import generate_response

def chatbot(query):
    results = search_knowledge_base(query)
    if not results:
        return "I'm sorry, I couldn't find any relevant information in my knowledge base."

    context = "\n".join([match['metadata']['text'] for match in results])
    response = generate_response(query, context)
    return response

if __name__ == "__main__":
    query = input("Enter your query: ")
    print(chatbot(query))
