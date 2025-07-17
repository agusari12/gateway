from flask import Flask, request
import requests

app = Flask(__name__)

# Token dan chat_id Telegram
BOT_TOKEN = "8033826325:AAG9vBAOphBkpuoFOjm25fuNtZ7D5sY38Lo"
CHAT_ID = "176979831"

@app.route("/")
def home():
    return "Gateway Telegram Aktif"

@app.route("/kirim", methods=["POST"])
def kirim():
    try:
        data = request.get_json()
        print("Data diterima:", data)  # Log ke Railway Console

        if not data or "pesan" not in data:
            return {"error": "Data kosong atau tidak lengkap"}, 400

        message = data["pesan"]
        print("Pesan yang akan dikirim:", message)

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(url, json=payload)
        print("Telegram response:", response.text)

        return {"status": "terkirim", "telegram_response": response.json()}
    except Exception as e:
        print("Error:", str(e))
        return {"status": "gagal", "error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
