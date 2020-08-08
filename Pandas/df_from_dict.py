import pandas as pd
row_list = {'KARNATAKA':[{'City' : 'Bangalore', 'Count' : 21},{'City' : 'Hubli', 'Count' : 22},{'City' : 'Mysore', 'Count' : 22}]}

df = pd.DataFrame(row_list)
print(df)