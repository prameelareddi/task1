from sentence_transformers import SentenceTransformer
import pinecone

model = SentenceTransformer('all-MiniLM-L6-v2')
pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")

index_name = "document-embeddings"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=384)

index = pinecone.Index(index_name)

def add_to_knowledge_base(sections):
    for section, content in sections.items():
        content_text = " ".join(content)
        embeddings = model.encode(content_text)
        index.upsert([(section, embeddings.tolist())])
