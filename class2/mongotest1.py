import pymongo

# client is the connectivity that we have created
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.tgtd0.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# # in mongo db d is referred to as document, the real data
# d = {
#     "name": "sudhandhu",
#     "email": "sudhanshu@ineuron.ai",
#     "surname": "kumar"
# }

# list_of_records is an example of json
list_of_records = [
    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'},

    {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Deep Learning for NLP and Computer vision'},

    {'companyName': 'iNeuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'}
]

# a database myinfo is being created
database = client['myinfo']
# collection is the collection of multiple documents
# in database a collection(equivalent to table in SQL)  has to be created
collection = database['sudh']
# inserting a record inside collection , in this case the document d
collection.insert_one(d)
# inserting the json in collection
collection.insert_many(list_of_records)
