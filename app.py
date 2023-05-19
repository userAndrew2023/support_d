import threading

from flask import Flask, request
from main import *

app = Flask(__name__)
threading.Thread(target=polling).start()


@app.route("/send")
def send():
    user_id = request.args.get("user_id")
    username = request.args.get("username")
    message = request.args.get("message")
    bot.send_message(user_id, f"Поступило новое сообщение от @{username}:\n\n<b>{message}</b>\n\n({user_id})", parse_mode="HTML")
    return "True"


if __name__ == '__main__':
    app.run(port=5001)
