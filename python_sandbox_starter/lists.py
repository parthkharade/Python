# A List is a collection which is ordered and changeable. Allows duplicate members.
# like arrays

number = [1,2,3,4,5]

# can also use a constructor

numbers2 = list((1,2,3,4,5))


#both of them do the exact same thing
print (number,numbers2)


fruits = ['Apples' , 'Oranges' , 'Grapes', 'Pears']

#Get a value from the list

print(fruits[1])
print(len(fruits))

#Append
fruits.append('Mangoes')

print(fruits)

#Remove

fruits.remove('Grapes')
print(fruits)

fruits.insert(2,'Strawberries')
print(fruits)

#remove with pop
fruits.pop(2)

print(fruits)

#reverse

fruits.reverse()
print(fruits)

#sort
fruits.sort()
print(fruits)

#sort reverse

fruits.sort(reverse= True)
print(fruits)