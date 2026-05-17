import chromadb
from chromadb.utils import embedding_functions
from core.config import settings
from google import genai
import uuid

# Configurar ChromaDB
chroma_client = chromadb.PersistentClient(path=settings.CHROMA_DB_PATH)
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-multilingual-MiniLM-L12-v2")

collection = chroma_client.get_or_create_collection(
    name="telesupport_calls",
    embedding_function=sentence_transformer_ef
)

# Configurar Gemini
client = genai.Client(api_key=settings.GOOGLE_API_KEY)

def add_to_rag(transcription: str, analysis: dict):
    doc_id = str(uuid.uuid4())
    collection.add(
        documents=[transcription],
        metadatas=[{
            "summary": analysis["summary"],
            "category": analysis["category"],
            "sentiment": analysis["sentiment"]
        }],
        ids=[doc_id]
    )

async def query_rag(user_query: str):
    # 1. Recuperar contexto do ChromaDB
    results = collection.query(
        query_texts=[user_query],
        n_results=3
    )
    
    context = ""
    for i, doc in enumerate(results['documents'][0]):
        meta = results['metadatas'][0][i]
        context += f"Chamada {i+1} (Categoria: {meta['category']}): {doc}\nResumo: {meta['summary']}\n\n"

    # 2. Gerar resposta final com Gemini usando o contexto
    prompt = f"""
    Você é um assistente da TeleSupport Angola. Use as seguintes informações de chamadas passadas para responder à pergunta do usuário.
    
    Contexto:
    {context}
    
    Pergunta do Usuário: {user_query}
    """

    response = client.models.generate_content(
        model=settings.MODEL_NAME,
        contents=prompt
    )

    return {
        "answer": response.text,
        "sources": results['metadatas'][0]
    }
