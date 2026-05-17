from faster_whisper import WhisperModel
from core.config import settings

def transcribe_audio(file_path: str):
    model = WhisperModel(settings.WHISPER_MODEL, device="cpu", compute_type="int8")
    segments, info = model.transcribe(file_path, beam_size=5)
    
    transcription = " ".join([segment.text for segment in segments])
    return transcription.strip()
