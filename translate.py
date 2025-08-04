import whisper
from googletrans import Translator
import sys
import os

# Check for audio file argument
if len(sys.argv) < 2:
    print("❌ Please provide the path to an audio file.")
    print("Usage: python3 dual_translate.py <filename.wav>")
    sys.exit(1)

audio_file = sys.argv[1]

# Check if file exists
if not os.path.isfile(audio_file):
    print(f"❌ File not found: {audio_file}")
    sys.exit(1)

# Load Whisper model
model = whisper.load_model("tiny")

# Transcribe
result = model.transcribe(audio_file)
english_text = result["text"]
print("\n🔤 English Transcription:\n", english_text)

# Translate to Hindi
translator = Translator()
hindi_translation = translator.translate(english_text, src='en', dest='hi')
print("\n🌐 Hindi Translation:\n", hindi_translation.text)
