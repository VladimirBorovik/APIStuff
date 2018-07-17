import json
import requests
import telepot


bot = telepot.Bot('661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0')
meta_info = bot.getMe()

print(meta_info)

#response = requests.get("https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8")
#json_data = json.loads(response.content)

#for item in json_data:
#17
#661730605:AAGMhc2ML5lxF5mxNCWIRqlT6g7Yk5z4p-0
#print(json_data['team']['name'])

