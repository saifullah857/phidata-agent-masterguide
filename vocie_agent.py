import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3

# ---------------- TTS ---------------- #

engine = pyttsx3.init()

# ---------------- RECORD ---------------- #

fs = 44100
seconds = 5

print("🎤 Speak now...")

audio = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1
)

sd.wait()

write("voice.wav", fs, audio)

print("✅ Recording Complete")

# ---------------- SPEECH TO TEXT ---------------- #

recognizer = sr.Recognizer()

with sr.AudioFile("voice.wav") as source:
    audio_data = recognizer.record(source)

text = recognizer.recognize_google(audio_data)

print("🗣 You Said:", text)

# ---------------- AI RESPONSE ---------------- #

response = f"You said: {text}"

print("🤖 AI:", response)

# ---------------- SPEAK RESPONSE ---------------- #

engine.say(response)
engine.runAndWait()