import pymongo
import pandas as pd 

myclient = pymongo.MongoClient("mongodb+srv://bitsps1:WJ70pOMfq8JOBQ42@fm-ps1-vquj0.gcp.mongodb.net/eshipz?retryWrites=true&w=majority")
mydb=myclient["eshipz"]

#db = pd.DataFrame(list(mydb))
print(type(mydb))
print(type(mydb))
#for order in mydb.orders.find({}):
#    print(order)
