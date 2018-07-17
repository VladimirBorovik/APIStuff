import telebot
from telebot import types

# токен
bot = telebot.TeleBot("")
# данные переменные были придуманы для контроля игры
# но проблема в том, что они влияют на все текущие сессии
# поэтому лучше создать словарь с ключами id сессий
flagTest1 = [True, True, True]
test = 0


# обработка команды /game
@bot.message_handler(commands=['game'])
def game_test(message):
    # создание клавиатуры - кнопок
    # callback_data - что вернется в функцию @bot.callback_query_handler(func = lambda call: True)
    # в переменной call.data
    keyboard = types.InlineKeyboardMarkup()
    call1 = types.InlineKeyboardButton(text="Кнопка1", callback_data="test ")
    call2 = types.InlineKeyboardButton(text="Кнопка2", callback_data="test1")
    call3 = types.InlineKeyboardButton(text="Кнопка2", callback_data="test2")
    keyboard.row(call1, call2, call3)
    bot.send_message(message.chat.id, "начнем игру", reply_markup=keyboard)


# реакция бота на текст
# очень важен порядок hadler так как команда - это текст, поэтому команды обрабатываем переж тесктом
@bot.message_handler(content_types=['text'])
def f(message):
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Привет, {0}".format(message.from_user.first_name))


# декоратор принимает функцию, которая выполняет роль фильтра
# срабатывает если результат True
# в данном случае ловлю все call
# и это не есть хорошо, лучше разбить на несколько обработчиков
# данный обработчик должен вызвать bot.register_next_step_handler(answer, func)
# т.е. действие callback
# принимает сообщение для пользователя и функцию обработчик
@bot.callback_query_handler(func=lambda call: True)
def call_back_request(call):
    if call.message:
        if call.data == "test":
            answer = bot.send_message(call.message.chat.id, "Какого цвета учебник?")
            func = test1
        elif call.data == "test1":
            answer = bot.send_message(call.message.chat.id, "Как называется предмет?")
            func = test2
        elif call.data == "test2":
            answer = bot.send_message(call.message.chat.id, "Как меня зовут?")
            func = test3
        bot.register_next_step_handler(answer, func)


def test1(answer):
    global test
    if not any(flagTest1):
        print("lose")
        bot.send_message(answer.chat.id, "ваш результат {0}".format(test))
    if flagTest1[0] == True:
        if answer.text.lower() == "красный":
            text = "Неплохо"
            test += 1
        else:
            text = "Вы даже книгу не открывали!!!!!"
        flagTest1[0] = False
        bot.send_message(answer.chat.id, text)
    else:
        bot.send_message(answer.chat.id, "Вы уже здесь были")


def test2(answer):
    global test
    if not any(flagTest1):
        print("lose")
        bot.send_message(answer.chat.id, "ваш результат {0}".format(test))
    if flagTest1[1] == True:
        if answer.text.lower() == "сопромат":
            if answer.text == "СОПРОМАТ":
                text = "Очень хорошо"
                test += 1
            else:
                text = "Не плохо"
        else:
            text = "очень плохо"
        flagTest1[1] = False
        bot.send_message(answer.chat.id, text)
    else:
        bot.send_message(answer.chat.id, "Вы уже здесь были")


def test3(answer):
    global test
    if not any(flagTest1):
        print("lose")
        bot.send_message(answer.chat.id, "ваш результат {0}".format(test))
    if flagTest1[2] == True:
        if answer.text.lower() == "николай":
            if answer.text == "Николай":
                text = "Очень хорошо"
                test += 1
            else:
                text = "Не плохо"
        else:
            text = "очень плохо"
        flagTest1[2] = False
        bot.send_message(answer.chat.id, text)
    else:
        bot.send_message(answer.chat.id, "Вы уже здесь были")


# запуск сервера с помощью polling
if __name__ == '__main__':
    bot.polling(none_stop=True)
