from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import speech_recognition as sr

app = Flask(__name__)
socketio = SocketIO(app)

# Variable pour garder l'état du bouton
is_running = False

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on("toggle_button")
def handle_toggle():
    global is_running
    is_running = not is_running
    emit("update_status", {"is_running": is_running}, broadcast=True)
    if is_running:
        # Lancer la reconnaissance vocale
        recognize_color()

def recognize_color():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dites une couleur : bleu, rouge, vert, jaune...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="fr-FR").lower()
            recognized_color = None
            if "bleu" in text:
                recognized_color = "bleu"
            elif "rouge" in text:
                recognized_color = "rouge"
            elif "vert" in text:
                recognized_color = "vert"
            elif "jaune" in text:
                recognized_color = "jaune"

            if recognized_color:
                print(f"Couleur reconnue : {recognized_color}")
                socketio.emit("recognized_color", {"color": recognized_color})
            else:
                print("Couleur non reconnue")
        except sr.UnknownValueError:
            print("Je n'ai pas compris la couleur")
        except sr.RequestError:
            print("Erreur de service de reconnaissance vocale")

if __name__ == "__main__":
    socketio.run(app, debug=True)
