from pymongo import MongoClient
import requests
import pymodm
import mongoengine

post = {"author": "Mike"}

response = requests.get(
    "https://api.sportradar.us/soccer-t3/eu/en/teams/sr:competitor:2/profile.json?api_key=rpjetjuheffkq2attc4g9hq8").json()

client = MongoClient('mongodb+srv://@cluster1-2yfbn.mongodb.net/test?retryWrites=true').get_database(
    name='Sport_Hub').get_collection(name='SHub')

insert_data = client.insert_one(document=response)