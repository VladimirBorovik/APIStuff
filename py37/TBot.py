import telepot
import requests
import Constants


class BotHandler:
    """Class which describes main logic for telegram bot."""

    def __init__(self, token: str) -> None:
        self.__userToken = token
        self.__botApi = f'https://api.telegram.org/bot{token}/'
        telepot.Bot(self.__botApi)

    @property
    def bot_api(self):
        return self.__botApi

    def get_updates(self) -> str:
        method = 'getUpdates'
        response = requests.get(str.join('', (self.bot_api, method))).json()
        return response

    def send_message(self, chat_id: int, text: str) -> str:
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        response = requests.post(str.join('', (self.bot_api, method)), params)
        return response

    def get_last_update(self) -> str:
        empty_str = ''
        get_result = self.get_updates()
        if len(get_result['result']) > 0 and get_result['ok'] is True:
            try:
                get_result = get_result['result'][-1]
            except KeyError as error:
                print(f'Data does not exist on dictionary by key {error}')
                return empty_str
        else:
            return empty_str
        return get_result

    def get_chat_id(self) -> int:
        last_update = self.get_last_update()
        if len(last_update['message']) > 0:
            try:
                last_update = last_update['message']['chat']['id']
            except KeyError as error:
                print(f'Can not match dictionary key {error}! Please try to check dictionary structure.')
                return -1
        return last_update

# bot = BotHandler(Constants.Token())

# bot.send_message(bot.get_chat_id(), 'Second message to personal Bot!')

# res = bot.get_updates()
# print(res['result'])
#
# last = bot.get_last_update()#
# print(bot.get_last_update())
#
# chat = bot.get_chat_id()
# print(chat)

# https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8
