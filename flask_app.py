from flask import Flask, request
from telegram import Bot
import config

app = Flask(__name__)
TOKEN = "7674017019:AAGNzTYltNuXueWyMgEZ6k-mEYqCw8jYpTc"
bot = Bot(token=TOKEN)

bot.set_webhook(config.get_url())

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()
    print(data)
    chat_id = data['message']['from']['id']
    first_name = data['message']['from']['first_name']
    if "text" in data['message']:
        text = data['message']['text']
        if text == '/start':
            bot.send_message(chat_id=chat_id, text= f"Hello {first_name}")
        else:
            bot.send_message(chat_id=chat_id, text= text)
    elif "photo" in data['message']:
        photo = data['message']['photo'][0]['file_id']
        bot.send_photo(chat_id, photo)

    elif "audio" in data['message']:
        audio = data['message']['audio']['file_id']
        bot.send_audio(chat_id, audio)

    elif "video" in data['message']:
        video = data['message']['video'][0]['file_id']
        bot.send_video(chat_id, video)

    elif "document" in data['message']:
        document = data['message']['document']['file_id']
        bot.send_document(chat_id, document)

    elif "animation" in data['message']:
        animation = data['message']['animation']['file_id']
        bot.send_latitude(chat_id, animation)

    elif "voice" in data['message']:
        voice = data['message']['voice']['file_id']
        bot.send_document(chat_id, voice)

    elif "contact" in data['message']:
        contact = data['message']['contact']['phone_number']
        first_name = data['message']['contact']['first_name']
        bot.send_contact(chat_id, contact, first_name)

    elif "location" in data['message']:
        latitude = data['message']['location']['latitude']
        longitude = data['message']['location']['longitude']
        bot.send_location(chat_id, latitude, longitude)

    return data

if __name__ == '__main__':
    app.run(port=8010, debug=True)