import pymongo



client = pymongo.MongoClient("mongodb+srv://hello:pN%24OsVc47NKi@cluster0-otwbz.gcp.mongodb.net/Lativa?retryWrites=true&w=majority")
db = client.Lativa


for doc in db.testOne.find():
        print(doc)