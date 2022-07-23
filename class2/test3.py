import pymongo

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]

# client is the connectivity that we have created
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.tgtd0.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['inventory']
collection = database["table"]
collection.insert_many(data)

# d = collection.find()
# d = collection.find({'status': "A"})
# any thing that starts with a $ is a reserved keyword
# d = collection.find({'status': {'$in': ['A','P']}})
# d = collection.find({'status': {'$gt': "C"}})
# d = collection.find({'qty': {'$gte': 75}})
# d = collection.find({'item':'sketch pad'}, {'qty': 95})
# d = collection.find({'item': 'sketch pad', 'qty': {'$gte': 75}}) # similar to AND condition
# d = collection.find({'$or' : [{'items': 'sketch pad'}, {'qty':{'$gte':75}}]})

# d = collection.find({'item':'canvas'}, {'$set': {'item': 'sudhanshu'}})
# d = collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })

# collection.delete_one({'item': 'sudhanshu'})
d = collection.find({'item': 'sudhanshu'})
for i in d:
    print(i)

# join os is same as the aggregatiomm as in mongodb.
