from flask import Flask, request, jsonify
import requests
import telebot

app = Flask(__name__)

# Telegram Bot API details
TELEGRAM_API_URL = "7843422944:AAGIl3EyW9__kjQvYbPhLEfVn19j7rfZd1c"
CHAT_ID = "<1616846358>"

# Инициализация Telegram-бота
bot = telebot.TeleBot(API_TOKEN)

# Главная страница (корневой путь)
@app.route('/')
def index():
    return "Server is running!"

# Путь для обработки сигналов
@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    print(f"Received signal: {data}")
    
    # Отправка сигнала в Telegram
    signal = data.get('signal')
    symbol = data.get('symbol')
    price = data.get('price')
    timeframe = data.get('timeframe')
    
    message = f"Signal: {signal}\nSymbol: {symbol}\nPrice: {price}\nTimeframe: {timeframe}"
    bot.send_message(CHAT_ID, message)
    
    return jsonify({"status": "success", "message": "Signal received and sent to Telegram!"})

# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

