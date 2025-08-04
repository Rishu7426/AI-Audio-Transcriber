# 🎙️ AI-Audio-Transcriber

AI-Audio-Transcriber is an open-source Python tool that converts spoken audio into readable text using OpenAI's Whisper model. It supports multiple audio formats and can translate transcriptions into various languages like English and Hindi. Ideal for developers, content creators, and accessibility tools.

---

## 1. 🚀 Features

1. 🎤 Convert audio files (WAV, MP3, etc.) into accurate transcriptions  
2. 🌐 Translate transcriptions to multiple languages (e.g., Hindi, English)  
3. 🧠 Built on OpenAI’s Whisper speech recognition model  
4. 💻 Simple command-line interface (CLI)  
5. 🔄 Easily extendable for custom voice assistant workflows

---

## 2. 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/AI-Audio-Transcriber.git
cd AI-Audio-Transcriber

# 2. Create and activate virtual environment
python3 -m venv venv && source venv/bin/activate

# 3. Install Whisper and required packages
pip install git+https://github.com/openai/whisper.git
pip install ffmpeg-python

# 4. Install FFmpeg (required for audio processing)
sudo apt update && sudo apt install ffmpeg -y

**## 5. 🎧 Usage**
# 1. Download a sample audio file
wget https://www2.cs.uic.edu/~i101/SoundFiles/StarWars3.wav -O test.wav

# 2. Run the transcriber with translation
python3 translate.py test.wav
