
import telepot
import requests

USER_TOKEN = '661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0'

message = 'From API!'
bot = telepot.Bot(USER_TOKEN)
meta_info = bot.getUpdates()


response = requests.get('https://api.telegram.org/bot661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0/getUpdates').json()
response = requests.get(
    "https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8")
print(response['result'])

res = bot.getChat(chat_id=190114760)

print(res)

# bot.sendMessage(chat_id=190114760, text=message)

#https://api.telegram.org/bot661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0/getUpdates

#print(meta_info)

#print(meta_info)

#response = requests.get("https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8")
#json_data = json.loads(response.content)

#for item in json_data:
#17
#661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0
#print(json_data['team']['name'])

