import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron_pratyu:Chahit1117@pratyusha.dc3s9sa.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "pratyusha",
    "email" : "pratyusha@gmail.com",
    "surname" : "ghanta"
}
d = {
    "name" : "pratyusha",
    "email" : "pratyusha@gmail.com",
    "surname" : "ghanta"
}

db1 = client['mongotest']
col1 = db1['test']
col1.insert_one(d)