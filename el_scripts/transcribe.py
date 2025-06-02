
import subprocess
import sys

#Check for a filename
if len (sys.argv) < 2:
    print ("Usage: python3.11 transcribe.py your_audio.wav")
    sys.exit(1)

#Get the file name
input_file = sys.argv[1]

#Path to Whisper Binary
whisper_path = "../build/bin/whisper-cli"

#Path to model 
model = "../models/ggml-base.bin"

#Command
command = [whisper_path, "-m", model, "-f", f"../{input_file}"]

#Run
subprocess.run(command)
