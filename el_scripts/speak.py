
import requests
import os
import time
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

os.makedirs("static", exist_ok=True)

VOICES = {
    "el": "iyjNciGCooG4sIxA3Euj",
    "funny_friend": "9d9EpBpx0pYv3ITz6Bqq",
    "calm_dad": "yLpsmn1Po3RkZ9tSUxjv",
    "wise_grandpa": "0lp4RIz96WD1RUtvEu3Q",
    "caring_mom": "cYctNG9CmLHHErrIh5s7",
    "loving_grandma": "cVd39cx0VtXNC13y5Y7z"
}

def text_to_speech(text, voice_name="el"):
    voice_id = VOICES.get(voice_name, VOICES["el"])  

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.3,
            "similarity_boost": 0.85
        }
    }

    timestamp = int(time.time())
    filename = f"static/output_{timestamp}.mp3"

    response = requests.post(url, json=payload, headers=headers)
    print(f"🎤 Generating voice using: {voice_name} → ID: {voice_id}")

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Audio saved as {filename}")
        return filename
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")
        return None


