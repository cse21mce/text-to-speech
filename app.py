from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import edge_tts
import asyncio

app = FastAPI()

# Dictionary of languages with corresponding voice names
LANGUAGES = {
    "english": "en-IN-NeerjaNeural",
    "hindi": "hi-IN-SwaraNeural",
    "urdu": "ur-PK-AsadNeural",
    "punjabi": "pa-IN-GaganNeural",
    "gujarati": "gu-IN-NiranjanNeural",
    "marathi": "mr-IN-AarohiNeural",
    "telugu": "te-IN-MohanNeural",
    "kannada": "kn-IN-GaganNeural",
    "malayalam": "ml-IN-MidhunNeural",
    "tamil": "ta-IN-PallaviNeural",
    "odia": "or-IN-BibhukalyaniNeural",
    "bengali": "bn-IN-TanishaaNeural",
    "assamese": "as-IN-YashicaNeural",
    "manipuri_meitei": "mni-IN-SanaNeural"  # Experimental voice
}

# Pydantic model for input validation
class TTSRequest(BaseModel):
    text: str
    language: str
    output_file: str

@app.post("/generate-tts/")
async def generate_tts(request: TTSRequest):
    lang = request.language
    if lang not in LANGUAGES:
        raise HTTPException(status_code=400, detail=f"Language '{lang}' is not supported.")
    
    voice = LANGUAGES[lang]
    output_file = request.output_file
    
    try:
        communicator = edge_tts.Communicate(request.text, voice=voice)
        await communicator.save(output_file)
        return {"message": f"TTS generated successfully and saved to {output_file}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
