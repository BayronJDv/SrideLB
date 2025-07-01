import os
from flask import Flask, redirect, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Habilita CORS para todos los orígenes

@app.route("/")
def root():
    active_color = os.getenv("ACTIVE_COLOR", "blue").lower()
    blue_url = os.getenv("BLUE_URL")
    green_url = os.getenv("GREEN_URL")

    if active_color == "blue" and blue_url:
        return redirect(blue_url, code=302)
    elif active_color == "green" and green_url:
        return redirect(green_url, code=302)
    else:
        return jsonify({"error": "Configuración inválida"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
