import speech_recognition as sr

def speech_to_text ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='pt-BR')
        print(f"User said: {text}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return speech_to_text()
    return text