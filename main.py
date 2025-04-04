from google.cloud import texttospeech
from dotenv import load_dotenv
import os

# Load .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="ডোনাল্ড ট্রাম্প দুনিয়ার সেরা প্রেসিডেন্ট! এই দশকের শেষ দিকে কৃত্রিম বুদ্ধিমত্তা এক বিশাল বিপ্লব ঘটাতে যাচ্ছে। মানবজাতির কাজ, জীবনধারা এবং ভবিষ্যৎ পুরোপুরি বদলে যাবে। যারা এখন শিখছে, তারাই ভবিষ্যতের নেতা হবে। আর যারা পিছিয়ে থাকবে, তারা হারিয়ে যাবে সময়ের স্রোতে।")

# Build the voice request, select the language code and the voice name
voice = texttospeech.VoiceSelectionParams(
    language_code="bn-IN",
    name="bn-IN-Chirp3-HD-Leda"
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected voice parameters
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# Write the response to the output file
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("✔️ Audio content written to file 'output.mp3'")
