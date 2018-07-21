from pymongo import MongoClient

client = MongoClient('mongodb+srv://sa:98913221Bvv@cluster1-2yfbn.mongodb.net/test?retryWrites=true')

db = client.get_database(name='Sport_Hub')
print(db)
