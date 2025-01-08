import subprocess
from pathlib import Path

def synthesize_speech(text: str, lang: str, output_file: str):
    model_path = f"app/models/{lang}/fastpitch/best_model.pth"
    config_path = f"app/models/{lang}/config.json"
    vocoder_path = f"app/models/{lang}/hifigan/best_model.pth"
    vocoder_config_path = f"app/models/{lang}/hifigan/config.json"
    
    if not Path(model_path).exists():
        raise FileNotFoundError(f"Model path {model_path} not found")
    
    cmd = [
        "python3", "-m", "TTS.bin.synthesize",
        "--text", text,
        "--model_path", model_path,
        "--config_path", config_path,
        "--vocoder_path", vocoder_path,
        "--vocoder_config_path", vocoder_config_path,
        "--out_path", output_file,
    ]
    
    subprocess.run(cmd, check=True)
