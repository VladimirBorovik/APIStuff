import http.client
import json
import requests



conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "soccer-t3/eu/en/teams/sr:competitor:1/profile.json?api_key=rpjetjuheffkq2attc4g9hq8")

res = conn.getresponse()
response = requests.get(res)
#data = res.read()

print(response.json())
#print(data.decode("utf-8"))
