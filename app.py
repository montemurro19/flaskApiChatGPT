from flask import Flask, jsonify, request, send_file
from services import speech_to_text, text_to_audio

app = Flask(__name__)

@app.route('/speech_to_text', method=['POST'])
def api_speech_to_text():

    response = speech_to_text(request.files['audio'])
    return jsonify(response)

@app.route('/text_to_audio', method=['POST'])
def api_text_to_audio():

    text = request.json['text']
    audio_file_path = text_to_audio(text)
    return send_file(audio_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()