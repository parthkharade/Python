# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create a tuple

fruits = ('Apples', 'Oranges', 'Grapes')
fruits2= tuple(('Apples', 'Oranges', 'Grapes'))

# If the tuple has a single element put a trailing comma, otherwise it will be treated as string

print(fruits,fruits2)
#get value
print(fruits[1])

#Cannot change value
# NOT ALLOWED fruits[0] = 'Pears'

#delete a tuple
del fruits2

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.


#create a set

fruits_set = {'Apples','Oranges','Mango'}

#check if in a set

print('Apples' in fruits_set)

#add to set

fruits_set.add('Grapes')
print(fruits_set)

#remove
fruits_set.remove('Grapes')
print(fruits_set)

#clear the set
#fruits_set.clear()
#print(fruits_set)

#does not add apples
fruits_set.add('Apples')
print(fruits_set)

# non-indexed print(fruits_set[3])

#delete
#del fruits_set


