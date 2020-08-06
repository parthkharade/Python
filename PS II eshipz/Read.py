import pymongo
import pandas as pd 

myclient = pymongo.MongoClient("mongodb+srv://bitsps1:WJ70pOMfq8JOBQ42@fm-ps1-vquj0.gcp.mongodb.net/eshipz?retryWrites=true&w=majority")

data = myclient.eshipz.orders.find()
db = pd.DataFrame(data)
db.to_csv('Orders.csv')
