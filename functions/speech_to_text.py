import os
import speech_recognition as sr

audio_path = os.path.abspath('audio/Gravando.wav')

def speech_to_text (audio_path):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
    except Exception as e:
        text = "Say that again please..."
    return text

print(speech_to_text(audio_path))