import telepot
import requests
import Constants


class BotHandler:
    """
    Class which describes main logic for telegram bot.
    """

    def __init__(self, token):
        self.__userToken = token
        self.__botApi = f'https://api.telegram.org/bot{token}/'
        telepot.Bot(self.__botApi)

    @property
    def bot_api(self):
        return self.__botApi

    def get_updates(self) -> str:
        method = 'getUpdates'
        response = requests.get(str.join('', (self.__botApi, method))).json()
        return response

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        response = requests.post(str.join('', (self.__botApi, method)), params)
        return response

    def get_last_update(self) -> str:
        get_result = self.get_updates()
        if len(get_result['result']) > 0:
            last_update = get_result['result'][-1]
        return last_update

    def get_chat_id(self) -> int:
        last_update = self.get_last_update()
        if len(last_update['message']) > 0:
            try:
                last_update = last_update['message']['chat']['id']
            except KeyError as error:
                print(f'Can not match dictionary key {error}! Please try to check dictionary structure.')
                return -1
        return last_update


bot = BotHandler(Constants.Token())
res = bot.get_updates()
print(res['result'])

last = bot.get_last_update()
print(bot.get_last_update())

chat = bot.get_chat_id()
print(chat)



# message = 'From API!'
# bot = telepot.Bot(__USER_TOKEN)
# meta_info = bot.getUpdates()


# response = requests.get('https://api.telegram.org/bot661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0/getUpdates').json()
# print(response['result'])

# res = bot.getChat(chat_id=190114760)

# print(res)

# bot.sendMessage(chat_id=190114760, text=message)

# https://api.telegram.org/bot661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0/getUpdates

# print(meta_info)

# print(meta_info)

# response = requests.get("https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8")
# json_data = json.loads(response.content)

# for item in json_data:
# 17
# 661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0
# print(json_data['team']['name'])
