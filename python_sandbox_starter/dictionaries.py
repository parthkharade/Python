 # A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. 

#create dictionary 
person = {
    'first name' : 'Parth',
    'last name'  : 'Kharade',
    'Age'        : 21}

#get value

print(person['first name'])
print(person.get('last name'))

#add a key/value
person['phone'] = '022-2544-5725'


#get dict items
print(person.items())

#copy a dictionary
person2 = person.copy()
person2['City'] = 'Thane'

print(person2)

#remove an item
del(person['Age'])
print(person)

person.pop('phone')
print(person)

#clear
person.clear()
print(person)

#get length
print(len(person2))

#creating list of dictionaries

people = [{'name' : 'Martha', 'age': 30},{'name' : 'Jonas', 'age': 30}]

#add a new dictionary ... people is an object of type list
print(people)
people.append({'Fruit': 'Apple', 'Status': 'Fresh'})
print(people)

#Add to a specific dictionary
people[0]['number'] = '999 999 9999'
print(people)
