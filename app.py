from flask import request, Response, Flask
from flask_cors import CORS
import pymongo
from bson.json_util import dumps
import json

app = Flask(__name__)
# fixing cors
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'
app.config["DEBUG"] = True

# Loads the Database and Collections

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-gjuwr.gcp.mongodb.net/safedb?retryWrites=true&w=majority")
db = pymongo.database.Database(client, 'safelys_1')


@app.route('/')
def home():
    return "Welcome to Safelys!"


@app.route('/test')
def test():
    return "Passed"


@app.route('/userlist')
def userlist():
    users = db.user
    return users.count_documents({})


@app.route('/new_store',methods=['POST'])
def new_store():
    inputData = request.json
    Store_Info = pymongo.collection.Collection(db, 'Store_Info')
    stores = json.loads(dumps(Store_Info.find({'store_name':inputData['store_name']})))
    if(len(stores) == 0):
        Store_Info.insert_one(inputData)
        return Response(status=200)
    else:
        Store_Info.update_one({'store_name':inputData['store_name']}, {'$set': inputData})
        return Response(status=200)


@app.route('/update_count',methods=['POST'])
def update_count():
    inputData = request.json
    Store_Info = pymongo.collection.Collection(db, 'Store_Info')
    stores = json.loads(dumps(Store_Info.find({'store_name':inputData['store_name']})))
    if(len(stores) == 0):
        return Response(status=404)
    else:
        Store_Info.update_one({'store_name':inputData['store_name']}, {'$set': inputData})
        return Response(status=200)

@app.route('/get_store_data')
def get_store_data():
    Store_Info = pymongo.collection.Collection(db, 'Store_Info')
    stores = json.loads(dumps(Store_Info.find()))
    retdata = dict()
    retdata['count'] = len(stores)
    retdata['data'] = stores
    return retdata


@app.route('/get_offer_data')
def get_offer_data():
    Offer_Info = pymongo.collection.Collection(db, 'Offer_Info')
    stores = json.loads(dumps(Offer_Info.find()))
    retdata = dict()
    retdata['count'] = len(stores)
    retdata['data'] = stores
    return retdata

@app.route('/get_order_data' ,methods=['POST'])
def get_order_data():
    inputData = request.json
    Order_Info = pymongo.collection.Collection(db, 'Order_Info')
    stores = json.loads(dumps(Order_Info.find(inputData)))
    retdata = dict()
    retdata['count'] = len(stores)
    retdata['data'] = stores
    return retdata


@app.route('/populate_store_info')
def populate_store_info():
    Input_Data = request.json
    Store_Info = pymono.collections.Collections(db, 'Store_Info')
    stores = json.loads(dumps(Store_info.find()))
    Store_Info.update_one({'store_name':inputData['store_name']}, {'$set': inputData})
    return Response(status=200)


@app.route('/add_new_offer',methods=['POST'])
def add_new_offer():
    inputData = request.json
    Offer_Info = pymongo.collection.Collection(db, 'Offer_Info')
    Offer_Info.insert_one(inputData)
    return Response(status=200)
