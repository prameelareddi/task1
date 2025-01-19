def search_knowledge_base(query, top_k=3):
    query_embedding = model.encode(query).tolist()
    results = index.query(query_embedding, top_k=top_k, include_metadata=True)
    return results['matches']
