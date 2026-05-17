from google import genai
from core.config import settings
import json
import asyncio

client = genai.Client(api_key=settings.GOOGLE_API_KEY)

async def process_call_analysis(transcription: str):
    prompt = f"""
    Analise a seguinte transcrição de uma chamada de suporte da TeleSupport Angola.
    Extraia o seguinte:
    1. Resumo conciso da chamada.
    2. Classificação da categoria (ex: Reclamação, Dúvida, Elogio, Cancelamento).
    3. Sentimento predominante (Positivo, Neutro, Negativo).

    Transcrição:
    {transcription}

    Responda EXCLUSIVAMENTE em formato JSON puro, sem markdown:
    {{
        "summary": "...",
        "category": "...",
        "sentiment": "..."
    }}
    """

    response = client.models.generate_content(
        model=settings.MODEL_NAME,
        contents=prompt
    )
    
    # Limpar a resposta caso venha com markdown
    text_response = response.text.strip()
    if text_response.startswith("```json"):
        text_response = text_response.replace("```json", "").replace("```", "").strip()
    
    return json.loads(text_response)
