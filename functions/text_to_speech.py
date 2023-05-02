from gtts import gTTS
import os

def text_to_speech(inputText):
    tts = gTTS(text = inputText, lang='pt-br')
    tts.save('./audio/audio.mp3')

    """ os.system('mpg321 audio.mp3') """