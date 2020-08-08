import pandas as pd
#First we will make a dictionary where keys are states and values are lists.
#The lists are lists of dictionaries where key is the city name and value is the count
#then we will make another dictionary where the key is the state and the value is a pandas dataframe converted from the above lists

flag = False
IN = pd.read_csv('Filtered.csv')
unique = IN['State'].unique()
dict = {}

for x in unique: #initialising a dictionary with empty lists
    dict[x] = {}
for x in IN.index:
    state = IN['State'][x]
    city  = IN['City'][x]
    y     = dict[state]
    if city in y.keys():
        dict[state][city] = dict[state][city]+1
    else:
        dict[state][city] = 1

dict2 = {}       
for x in unique:
    dict2[x] = pd.DataFrame([dict[x]])

list = []
for x in unique:
    df = dict2[x]
    for y in df:
        list.append({'City' : y,'Count' : dict2[x][y][0]})
    df = pd.DataFrame(list)
    dict2[x]=df
    list.clear()

top_del = pd.DataFrame(columns=['State','City','Count'])
top_del_row = 0
for x in unique:
    dict2[x]=dict2[x].sort_values(by='Count',ascending = False)
    dict2[x]=dict2[x].reset_index(drop=True)
    top_del.loc[top_del_row] = x,dict2[x]['City'][0],dict2[x]['Count'][0]
    top_del_row +=1

top_del=top_del.sort_values(by='Count',ascending = False)
top_del=top_del.reset_index(drop=True)
print(top_del)

top_del.to_csv('Top_Deliver_ByState.csv')
for x in unique:
    df = dict2[x]
    name = x+'.csv'
    df.to_csv(name)



