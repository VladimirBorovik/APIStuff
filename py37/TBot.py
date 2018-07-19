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

    def bot_api(self):
        self.__botApi = f'https://api.telegram.org/bot{token}/'

    def get_updates(self):
        method = 'getUpdates'
        response = requests.get(self.__botApi + method).json()
        return response


bot = BotHandler(Constants.Token())
res = bot.get_updates()
print(res)

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
