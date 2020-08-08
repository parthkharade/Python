import pandas as pd
from ast import literal_eval
db  =   pd.read_csv('Orders.csv')

db  =   db['order_details']

PIN =   pd.read_csv('PIN.csv')

i   = 0

PIN.pincode = PIN.pincode.astype(str) #typecast the pincode values as string

IN = pd.DataFrame(columns = ['State','City'])   #creating a dataframe to store the states and the cities
IN_row = 0

x   = pd.DataFrame()

for a in db:
    a  = literal_eval(a)
    if(a['receiver_address']['country'] == 'IN'):
        x = PIN.loc[PIN['pincode'] == a['receiver_address']['postal_code']]
        x = x.loc[~(x['Taluk'] !=x['Taluk'])]
        if(len(x.index)>0):
            x = x.iloc[0]
            IN.loc[IN_row] = x['statename'],x['Taluk']
            IN_row = IN_row + 1
IN.to_csv('Filtered.csv')
print(IN)