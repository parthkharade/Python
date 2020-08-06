import pandas as pd
db = pd.read_csv('Orders.csv')

db = db['order_details']

IN = pd.DataFrame(columns = ['State','City'])

IN_row = 0

for a in db:
    if(a['receiver_address']['country'] == 'IN'):
        IN.loc[IN_row] = [a['receiver_address']['state'], a['receiver_address']['city']]
        IN_row = IN_row + 1

