import pymongo
client = pymongo.MongoClient("mongodb+srv://jchavez:kub0s911@cluster0.sqozq.mongodb.net/selfity?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority")
db = client.test