from gtts import gTTS

def text_to_audio(text):
    audio_file = gTTS(text)
    audio_file_path = 'audio.mp3'
    audio_file.save(audio_file_path)
    return audio_file_path