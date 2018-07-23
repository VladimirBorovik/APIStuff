from pymongo import MongoClient

client = MongoClient('')

db = client.get_database(name='Sport_Hub')
print(db)
