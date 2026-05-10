from flask import Flask, jsonify, request

app = Flask(__name__)

ACCESS_KEY = "sua_chave_aqui"

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "api": "Night Store"
    })

@app.route("/auth")
def auth():

    token = request.headers.get("Authorization")

    if token != ACCESS_KEY:
        return jsonify({
            "error": "Não autorizado"
        }), 401

    return jsonify({
        "success": True,
        "message": "Autorizado"
    })

app.run(host="0.0.0.0", port=3000)