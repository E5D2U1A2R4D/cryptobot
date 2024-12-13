from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Telegram Bot API details
TELEGRAM_API_URL = "7843422944:AAGIl3EyW9__kjQvYbPhLEfVn19j7rfZd1c"
CHAT_ID = "<1616846358>"

@app.route('/api/signal', methods=['POST'])
def handle_signal():
    try:
        # Get the data from TradingView
        data = request.get_json()

        symbol = data['symbol']
        timeframe = data['timeframe']
        signal = data['signal']
        price = data['price']

        # Prepare the message
        message = f"Signal: {signal}\nSymbol: {symbol}\nTimeframe: {timeframe}\nPrice: {price}"

        # Send message to Telegram
        send_to_telegram(message)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def send_to_telegram(message):
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(TELEGRAM_API_URL, data=payload)
    if response.status_code != 200:
        print(f"Failed to send message to Telegram. Error: {response.text}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
