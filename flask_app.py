from flask import Flask, request
from telegram import Bot
import config

app = Flask(__name__)
TOKEN = "7674017019:AAGNzTYltNuXueWyMgEZ6k-mEYqCw8jYpTc"
bot = Bot(token=TOKEN)

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    chat_id = data['message']['from']['id']
    text = data['message']['text']
    first_name = data['message']['from']['first_name']
    if text == '/start':
        bot.send_message(chat_id=chat_id, text= f"Hello {first_name}")
    else:
        bot.send_message(chat_id=chat_id, text= text)
    print(data)


    return data

@app.route('/home')
def home():
    return "Hello world"

if __name__ == '__main__':
    app.run(port=8080, debug=True)