# Python has functions for creating, reading, updating, and deleting files.

myfile = open('myfile.txt','w') #name , mode


#get some info

print('Name :', myfile.name)
print('Is Closed:', myfile.closed)
print('Mode :',myfile.mode)

#Write to a file
myfile.write('Pyhton tutorials \n')
myfile.write('Almost Done')
myfile.close()
print('Is Closed:', myfile.closed)

#append
myfile = open('myfile.txt','a')
myfile.write(' Almost Done')
myfile.close()

#read

myfile = open('myfile.txt','r+')
text = myfile.read(100)
print(text)