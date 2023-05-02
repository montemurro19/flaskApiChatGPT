import os
import speech_recognition as sr

def speech_to_text(audio_file):
    audio_file.save('audio.wav')

    r = sr.Recognizer()

    with sr.AudioFile('audio.wav') as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
        os.remove('audio.wav')
        return {'text': text}
    except sr.UnknownValueError:
        os.remove('audio.wav')
        return {'error': 'Não foi possível reconhecer o áudio'}
    except sr.RequestError as e:
        os.remove('audio.wav')
        return {'error': 'Erro ao se comunicar com o serviço de reconhecimento de fala'}
