from google.cloud import texttospeech
from dotenv import load_dotenv
from pydub import AudioSegment
from utils import split_text_by_bytes
import os

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Read Bangla script from file
with open("text/translated_bn.txt", "r", encoding="utf-8") as file:
    bangla_script = file.read()

# Split the full text into chunks under 5000 bytes
chunks = split_text_by_bytes(bangla_script)

# Set up Google Cloud TTS client
client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
    language_code="bn-IN",
    name="bn-IN-Chirp3-HD-Leda"
    # name="bn-IN-Chirp3-HD-Charon"
)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Prepare empty final audio segment
final_audio = AudioSegment.empty()

# Synthesize each chunk and append to final audio
for idx, chunk in enumerate(chunks):
    print(f"🎙️ Synthesizing chunk {idx + 1} of {len(chunks)}...")

    input_text = texttospeech.SynthesisInput(text=chunk)
    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    chunk_filename = f"output_chunk_{idx + 1}.mp3"
    with open(chunk_filename, "wb") as out:
        out.write(response.audio_content)

    final_audio += AudioSegment.from_file(chunk_filename, format="mp3")

# Export combined audio
final_audio.export("output.mp3", format="mp3")
print("✅ Final audio created as 'output.mp3'")
