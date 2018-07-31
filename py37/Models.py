from pymongo import MongoClient
import requests
import pymodm
import mongoengine

post = {"author": "Mike"}

# response = requests.get(
#    "https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:2/profile.json?api_key=rpjetjuheffkq2attc4g9hq8").json()

# client = MongoClient('mongodb+srv://sa:98913221Bvv@cluster1-2yfbn.mongodb.net/test?retryWrites=true').get_database(
#   name='Sport_Hub').get_collection(name='SHub')

# insert_data = client.insert_one(document=response)

client = MongoClient('mongodb+srv://sa:98913221@cluster2-usfat.mongodb.net/test?retryWrites=true') \
    .get_database(name='MovieStorage') \
    .get_collection('MovieRate')

print(client.name)

response = requests.get('http://www.omdbapi.com/?t=The+Godfather&plot=full&apikey=b792ed2a').json()
print(response)

responseWeatherForecast = requests.get(
    'http://dataservice.accuweather.com/forecasts/v1/daily/1day/11?apikey=nLIsTMwLA6fGbwAGdU7RjemBFA3HgT6l&details=true&metric=true').json()
print(responseWeatherForecast)

# forecast url -- 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/11?apikey=nLIsTMwLA6fGbwAGdU7RjemBFA3HgT6l&details=true&metric=true'

# insert_data = client.insert_one(document=response)
