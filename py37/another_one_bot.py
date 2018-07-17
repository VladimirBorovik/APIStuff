# пример использования различных сервисов скрипт (функция main)+ телеграмм
# каждый их этих объектов создает внутренний loop, что не дает стартовать
# другим loop
# решение использовать потоки

# данная программа следит за состоянием папки определенной в переменной basedir
# используя сериализацию для восстановления контактов после "смерти"
import telebot
from telebot import types
import pickle
import tkinter
import threading
import os
import time
import atexit
import sys

basedir = "C:\\test"
ls_file = []
flag = [True]
# определен админ
admin = 222443632
contact = {}
bot = telebot.TeleBot('')


def log():
    with open("t.b", "wb") as f:
        pickle.dump(ls_file, f)


def begin():
    if not os.path.exists("t.b"):
        ls_file.extend(os.listdir(basedir))
        ls_file.sort()
        log()
        return
    with open("t.b", "rb") as f:
        ls_ = pickle.load(f)
        ls_file.extend(ls_)


def send_message(message):
    with open("log.txt", "a") as f:
        f.writelines("//".join(str(item) for item in time.localtime()))
        f.write('\n')
        f.write(message)
        f.write('\n')
    for item in conntact:
        bot.send_message(item, message)


@bot.message_handler(commands=['edit'])
def edit(message):
    if message.chat.id != admin:
        return
    keyboard = types.InlineKeyboardMarkup()
    but = []
    for item in contact:
        but.append(
            types.InlineKeyboardButton(text="{} {}".format(*contact[item]), callback_data="edit {}".format(item)))
    keyboard.add(*but)
    bot.send_message(admin, "Ваш список контактов", reply_markup=keyboard)


@bot.message_handler(commands=['add'])
def action(message):
    keyboard = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text="Yes", callback_data="test {} {} {}".format(message.chat.id,
                                                                                        message.from_user.first_name,
                                                                                        message.from_user.last_name))
    call2 = types.InlineKeyboardButton(text="NO", callback_data="test1 {}".format(message.chat.id))
    keyboard.row(call1, call2)
    question = "Разрешить контакту {} {}".format(message.from_user.first_name, message.from_user.last_name)

    bot.send_message(admin, question, reply_markup=keyboard)

    # if answer.text=="Yes":
    #     conntact.append(message.chat.id)


@bot.callback_query_handler(func=lambda call: True)
def call_back_request(call):
    if call.message:
        data = call.data.split()
        new = int(data[1])
        if data[0] == "test":
            contact[new] = (data[2], data[3])
            bot.send_message(new, "Вы добавлены в список")
        else:
            bot.send_message(new, "Вам запрещено редактирование")


@bot.message_handler(content_types=['text'])
def command(message):
    id = message.chat.id
    text = message.text
    if id == 222443632 and text == "2":
        print("Ok")
        sys.exit(1)


def main():
    if flag[0]:
        begin()
        flag[0] = False
    while True:
        data = os.listdir(basedir)
        if data != ls_file:
            if (len(data) > len(ls_file)):
                new = [item for item in data if item not in ls_file]
                ls_file.extend(new)
                action = "add:\n"
            else:
                action = "delete:\n"
                new = [item for item in ls_file if item not in data]
                for item in new:
                    ls_file.remove(item)
            message = "\n".join(new)
            send_message(message=action + message)
            ls_file.sort()
            log()
        # если не указать прерывание - нагрузка на проц 100%
        # 5 секурдный интервал - нагрузка 0%
        time.sleep(5)
    atexit.register(good_bye)


def good_bye():
    send_message("good_bye")


def start():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    a = threading.Thread(target=start)
    b = threading.Thread(target=main)
    a.start()
    b.start()
    a.join()
    b.join()
