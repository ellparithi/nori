 # Nori

**Nori** is a voice-based AI companion designed to let users talk to an AI in natural language and receive lifelike responses using a cloned voice. Built as a minimal web app for immersive, ephemeral, real-time conversation, Nori runs locally with no cloud dependency.

##  Features

-  Record voice input via browser
-  Transcribe using Whisper (Python module)
-  Generate replies using OpenAI GPT-3.5
-  Convert replies to voice using ElevenLabs (custom voice)
-  Glacial ripple animation and voice bubble interface
-  Toggle between Python Whisper and whisper.cpp (optional)
-  Docker-ready setup for containerized deployment

##  Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **AI**: OpenAI GPT-3.5, Whisper, ElevenLabs
- **Audio**: ffmpeg, Web Audio API
- **Deployment**: Docker

##  Setup

### Prerequisites

- Python 3.11+
- `ffmpeg`
- OpenAI API key
- ElevenLabs API key and Voice ID

### Local Development

1. Clone the repo:
    ```bash
    git clone https://github.com/ellparithi/nori.git
    cd nori
    ```

2. Create `.env` file:
    ```env
    OPENAI_API_KEY=your-openai-key
    ELEVENLABS_API_KEY=your-elevenlabs-key
    ELEVENLABS_VOICE_ID=your-voice-id
    USE_PYTHON_WHISPER=true
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    flask run
    ```

5. Visit: [http://localhost:5000](http://localhost:5000)


##  Credits

Built by Elamparithi Elango
Voice cloning powered by [ElevenLabs](https://www.elevenlabs.io)  
Transcription by [Whisper](https://github.com/openai/whisper)

---

*“Talk to someone who sounds just like you.”*
