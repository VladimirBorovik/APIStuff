import json
import requests
import telepot

response = requests.get("https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8")
json_data = json.loads(response.content)

#for item in json_data:

print(json_data['team']['name'])
