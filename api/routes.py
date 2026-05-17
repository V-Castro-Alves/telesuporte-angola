from fastapi import APIRouter, UploadFile, File, HTTPException
from services.audio_service import transcribe_audio
from services.gemini_service import process_call_analysis
from services.rag_service import add_to_rag, query_rag
import os

router = APIRouter()

@router.post("/process-call")
async def process_call(file: UploadFile = File(...)):
    # 1. Salvar arquivo temporário
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        buffer.write(await file.read())
    
    try:
        # 2. Transcrição
        transcription = transcribe_audio(temp_file)
        
        # 3. Análise com Grok (Sumarização e Classificação)
        analysis = await process_call_analysis(transcription)
        
        # 4. Salvar no RAG
        add_to_rag(transcription, analysis)
        
        return {
            "filename": file.filename,
            "transcription": transcription,
            "analysis": analysis
        }
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

@router.get("/search")
async def search_calls(query: str):
    results = await query_rag(query)
    return {"results": results}
