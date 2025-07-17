from flask import Flask, request
import requests

app = Flask(__name__)

# Ganti dengan token dan chat_id Telegram kamu
BOT_TOKEN = "8033826325:AAG9vBAOphBkpuoFOjm25fuNtZ7D5sY38Lo"
CHAT_ID = "176979831"

@app.route("/kirim", methods=["POST"])
def kirim():
    data = request.get_json()
    if not data:
        return {"error": "Data kosong"}, 400

    message = data.get("pesan", "Tidak ada pesan")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, json=payload)
        return {"status": "terkirim", "telegram_response": response.json()}
    except Exception as e:
        return {"status": "gagal", "error": str(e)}, 500

@app.route("/")
def home():
    return "Gateway Telegram Aktif"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
