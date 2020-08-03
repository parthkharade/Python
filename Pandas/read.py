import pandas as pd

df = pd.read_csv('pokemon_data.csv')


#print the starting data
#print(df.head(3))

#can also load in excel files and/or tab seperated file

# df_xlsx = pd.read_excel('pokemon_data.xlsx')

# print(df_xlsx.head(3))


# df_txt = pd.read_csv('pokemon_data.txt',delimiter='\t')

# print(df_txt.head(3))


#READING HEADERS

#print(df.columns)

#READ EACH COLUMN

#print(df['Name'][0:5])

#READ MULTIPLE COLUMNS
#print(df[['Name','Type 1','HP']])

#READ EACH ROW

#print(df.iloc[1]) #iloc = Integer Location

#READ A SPECIFIC LOCATION

#print(df.iloc[2,1])

# for Index,Row in df.iterrows(): #index is the line number and Row is the Row's data
#     print(Index, Row['Legendary'])

#Finding data based on Textual Information
#Printing only those which have type 1 = fire
print(df.loc[df['Type 1'] == 'Fire'])



