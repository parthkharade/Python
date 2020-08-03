import pandas as pd
import re #Regular Expression

df = pd.read_csv('pokemon_data.csv')

# #Print Grass Pokemons whose names start with C
# x  = df.loc[(df['Type 1'] == 'Grass')]
# x  = x['Name']
# for y in x:
#     if(y[0] == 'C'):
#         print(y)

# #Grass and posion Pokemons
# x  = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
# print(x)
# x.reset_index(drop = True, inplace =True) #reset and drop the previous index without new declaration
# x.to_csv('filtered.csv')
# #Use the | and & signs when using pandas libraries

#Suppose We want to filter out everything with Mega

# mega = df.loc[~df['Type 1'].str.contains('Mega')]
# print(mega)

#Print with Type 1 = fire or grass ignore case = true regular expression = true

# fORg = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
# print(fORg)


# #Print name starting with Pi
# fORg = df.loc[df['Name'].str.contains('^Pi[a-z]*', flags=re.I, regex=True)] 
# print(fORg)

# #Replace the word Fire with Flamer
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# print(df)

#Adding a new column called Flamer.. Multple Columns can be modified at a time
df.loc[df['Type 1'] == 'Fire', 'New Attr'] = 'Flamer'
#print(df)

#putting the new attribute after Type 2
x = list(df.columns)
t2 = x.index('Type 2')
len= len(x)
df = df[x[0:t2+1]+[x[-1]]+x[t2+1:len-1]]
print(df)

#Going back to the original version
df = pd.read_csv('Modified.csv')