import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#SORTING
#print(df.sort_values(['Type 1', 'HP'], ascending =[1,0])) # pass ascending value for both columns

#making changes to the data

#1 adding stats to find SUPER STAT TO RANK POKEMONS

df['Total'] = df['HP'] + df['Attack'] + df['Defense']+	df['Sp. Atk']+ df['Sp. Def']+df['Speed']

#print(df.head(5))

df = df.drop(columns=['Total']) #reassignment is necessary

#print(df.head(5))

#Adding in a better way

df['Total'] = df.iloc[:,4:10].sum(axis=1) #axis = 1 means horizontal sum

#print(df.head(5))

#Inserting the total at some other place

cols = list(df.columns) #keep checking documentation

print(cols)

df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df)


# #To Get Index of column
# print(df.columns.get_loc('Legendary'))
# #To get index of row
# print(df.rows.get_loc('719'))


#Print Legendary Pokemons with 50 HP
for Index,Rows in df.iterrows():
    if((Rows['Legendary'] == True) & (Rows['HP'] == 50)): #put conditionals in brackets
            print(Rows['Name'], Rows['HP'])

#Saving as  CSV File

df.to_csv('Modified.csv', index=False) #save without the index

df.to_excel('Modified.xlsx',index=False)

df.to_csv('Modified.txt', index=False, sep='\t') # Note that there is no delimeter parameter, it is sep instead

