from flask import Flask, request, render_template
import subprocess
import os
import time
from generate_reply import generate_reply, conversation_history
from speak import text_to_speech

app = Flask(__name__)

conversation = []

@app.route("/", methods=["GET"])
def landing():
    return render_template("landing.html")

@app.route("/chat", methods=["GET", "POST"])
def index():
    transcript = ""
    el_reply = ""
    voice_name = request.form.get("voice") or request.args.get("voice", "el")

    if request.method == "GET":
        conversation.clear()
        from generate_reply import conversation_history
        conversation_history.clear()

    if request.method == "POST":
        file = request.files["audiofile"]

        if file:
            filename = "uploaded.wav"
            filepath = os.path.join("uploads", filename)
            os.makedirs("uploads", exist_ok=True)
            file.save(filepath)
            print("Received file:", file.filename)

            # Convert to Whisper-compatible format
            converted = "converted.wav"
            os.system(f"ffmpeg -y -i {filepath} -ar 16000 -ac 1 -c:a pcm_s16le {converted}")
            os.system(f"ffmpeg -i {filepath}")

            whisper_path = "../build/bin/whisper-cli"
            model = "../models/ggml-base.bin"

            result = subprocess.run(
                [whisper_path, "-m", model, "-f", converted],
                capture_output=True,
                text=True
            )

            print("Whisper output:\n", result.stdout)
            print("Whisper stderr:\n", result.stderr)
            transcript = result.stdout

            
            timestamp = int(time.time())
            parent_audio_path = f"static/parent_{int(time.time())}.wav"
            os.system(f"ffmpeg -y -i {filepath} -ar 16000 -ac 1 -c:a pcm_s16le {parent_audio_path}")


            conversation.append({
                "speaker": "Parent",
                "text": transcript,
                "audio": parent_audio_path
            })

            el_reply = generate_reply(transcript)
            print("El says:", el_reply)

            print("🔈 Using voice:", voice_name)

            el_audio_path = text_to_speech(el_reply, voice_name)

            conversation.append({
                "speaker": "El",
                "text": el_reply,
                "audio": el_audio_path  
            })

    return render_template("chat.html", conversation=conversation, voice_name=voice_name)


if __name__ == "__main__":
    app.run(debug=True)

