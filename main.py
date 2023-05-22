import requests
from telebot import *
from config import *

bot = TeleBot(token=TOKEN)
start_text = "Привет! Это бот поддержка Добби Seller. Сюда вам будут приходить обращения от " \
             "клиентов из бота Dobby.Seller. Чтобы ответить, ответьте на сообщение, которое " \
             "прислал бот"


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(func=lambda message: message.reply_to_message)
def reply_handler(message: types.Message):
    if message.reply_to_message.text == start_text:
        bot.send_message(message.chat.id, f"Вы ответили на сообщение бота при старте. Ваше сообщение: '{message.text}'."
                                          f" Также отвечайте на сообщения,"
                                          "которые будут приходить здесь 🙂")
    elif not message.reply_to_message.text.__contains__("Вы ответили на сообщение пользователя"):
        user = "@" + message.reply_to_message.text.split(":")[0].split('@')[1]
        user_id = "@" + message.reply_to_message.text.split("(")[1].replace(")", "")
        bot.send_message(message.chat.id, f"Вы ответили на сообщение пользователя {user} сообщением:\n\n"
                                          f"<b>{message.text}</b>", parse_mode="HTML")
        requests.get(f"http://127.0.0.1:5000/support?message={message.text}&user_id={user_id}")


def polling():
    bot.infinity_polling()
