import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.tgtd0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sudhandhu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}

db1 = client['mongotest']
call = db1['test']
call.insert_one(d)