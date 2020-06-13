import flask
from flask_cors import CORS
import pymongo
from bson.json_util import dumps
import json

app = flask.Flask(__name__)
# fixing cors
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'
app.config["DEBUG"] = True

# Loads the Database and Collections
# mongo = pymongo.MongoClient(
#     'mongodb+srv://admin:admin@cluster0-gjuwr.gcp.mongodb.net/safedb?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
# db = pymongo.database.Database(mongo, 'safedb')

# client = pymongo.MongoClient(
#     "mongodb+srv://admin:admincluster0-gjuwr.gcp.mongodb.net/safedb?retryWrites=true&w=majority")
# db = client.safedb

# mongo = pymongo.MongoClient(
#     'mongodb+srv://srujandeshpande:mongodb@cluster0-e0fen.azure.mongodb.net/test?retryWrites=true&w=majority', maxPoolSize=50, connect=True)
# db = pymongo.database.Database(mongo, 'covid_v1')

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0-gjuwr.gcp.mongodb.net/safedb?retryWrites=true&w=majority")
db = client.safedb


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/test')
def test():
    return "Passed"


@app.route('/userlist')
def userlist():
    users = db.user
    return users.count_documents({})


app.run()
