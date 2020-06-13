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

client = pymongo.MongoClient(
    "mongodb+srv://admin:admin@cluster0-gjuwr.gcp.mongodb.net/safedb?retryWrites=true&w=majority")
db = client.safedb


@app.route('/')
def home():
    return "sup"


@app.route('/test')
def test():
    return "Passed"


@app.route('/userlist')
def userlist():
    users = db.user
    return users.count_documents({})

@app.route('/update_count',methods=['POST'])
def update_count():
    try:
        inputData = request.json
        shop_details=db.shop_details
        newdata["count"] = inputData["count"]
        shop_details.update_one({"store_id":"mayura"},{"$set":newdata})
        return ({"status":"200"})
    except:
        return ({"status":"403"})