from flask import Flask, request, jsonify, abort
import os, uuid
import whisper
import threading

# Set the maximum allowed file size, e.g., for 10MB max file size:
MAX_FILE_SIZE = 10  * 1024 ** 2 
WHISPER_MODEL = whisper.load_model(os.environ["WHISPER_MODEL"])

# Create a Flask instance with bind IP address change
app = Flask(__name__)
SERVER_NAME = "localhost"
UPLOADS_DIR = "/svc/uploads"

@app.route("/api/transcribe", methods=["POST"])
def transcribe():

    # Get the file from the POST request

    try:
        data = request.stream.read()

        # Save the data to the configured uploads folder
        filename = str(uuid.uuid4()) + ".mp3"
        save_location = f"/svc/uploads/{filename}"
        with open(save_location, "wb") as song:
            song.write(data)

        audio = whisper.load_audio(save_location)
    
        result = WHISPER_MODEL.transcribe(save_location)
        os.remove(save_location)
        return {
            "language": result["language"],
            "text": result["text"]
        }
    except:
        return abort(500)

if __name__ == "__main__":
    port = 5000
    app_thread = threading.Thread(target=app.run, args=("0.0.0.0",port,))
    app_thread.start()