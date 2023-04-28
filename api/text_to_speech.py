import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    engine.setProperty('voice', 'brazil')

    engine.say(text)
    engine.runAndWait()