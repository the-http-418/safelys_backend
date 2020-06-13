import pymongo
# from bson.json_util import dumps

# Loads the Database and Collections

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0-gjuwr.gcp.mongodb.net/safedb?retryWrites=true&w=majority")
db = client.safedb

# mongo = pymongo.MongoClient(
#     'mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
# db = pymongo.database.Database(mongo, 'covid_v1')

users = db.user
print(
    users.count_documents({})
)
