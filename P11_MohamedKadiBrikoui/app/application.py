from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index():
    # Devuelve el nombre del host para saber qué contenedor responde
    return f"Hola desde {socket.gethostname()}"

@app.route("/status")
def status():
    return {
        "instancia": socket.gethostname(),
        "estado": "OK"
    }