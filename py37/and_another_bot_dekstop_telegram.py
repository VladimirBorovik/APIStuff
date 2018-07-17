import telebot
from telebot import types
import pickle
import tkinter
import threading
import os

bot = telebot.TeleBot('')


@bot.message_handler(commands=['game'])
def game_keep(message):
    print("Press")
    keyboard = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text="Вопрос1", callback_data="test")
    call2 = types.InlineKeyboardButton(text="Вопрос2", callback_data="time")
    keyboard.row(call1, call2)
    bot.send_message(message.chat.id, "test_test", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def f(message):
    bot.send_message(message.chat.id, message.chat.id)


# @bot.message_handler(content_types=["text"])
# def repeat(message):
#     print("one")
#     key = message.chat.id
#     data={}
#     try:
#         with open('text.b','rb') as f:
#             data=pickle.load(f)
#         i=data[key]
#     except:
#         i=0
#     bot.send_message(message.chat.id, i)
#     i+=1
#     data[key]=i
#     with open('text.b', 'wb') as f:
#         pickle.dump(data, f)


@bot.callback_query_handler(func=lambda call: True)
def callback_request(call):
    if call.message:
        if call.data == "test":
            answer = bot.send_message(call.message.chat.id, "Сколько лет Академиии Шаг?")
            func = test
        elif call.data == "time":
            answer = bot.send_message(call.message.chat.id, "Какая первая космическая скорость?")
            func = test2
        bot.register_next_step_handler(answer, func)


def test2(answer):
    if answer.text == "7.9":
        text = "Отлично, вы оказывается знаток"
    else:
        text = "Вам стоит подучить"
    bot.send_message(answer.chat.id, text)


def test(answer):
    if answer.text == "18":
        text = "Хорошо"
    else:
        text = "Очень плохо"
    bot.send_message(answer.chat.id, text)


def send_message():
    # data = os.listdir()
    bot.send_message(222443632, "Hello, my friend!!!")


# отправляете сообщения боту)))
def f1():
    tk = tkinter.Tk()
    but = tkinter.Button(tk, text="send_message", command=send_message)
    but.pack()
    tk.mainloop()


def f2():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    a = threading.Thread(target=f1)
    b = threading.Thread(target=f2)
    a.start()
    b.start()
    a.join()
    b.join()
