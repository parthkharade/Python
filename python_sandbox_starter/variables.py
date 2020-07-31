# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 1           #int
y = 2         #float
name = 'John'   #str allows both single and double quotes
is_cool = True  # bool , use capital T

#Multiple Assigments
x, y, name, is_cool = (1,2.5,'John',True)

#print() for giving outputs

print("Hello")

#basic math

a = x+y
print (a) #prints x

print (x+y) #prints x+y

#typecasting

x = str(x)
#y = str(y) 
#print(type(x),type(y),(x+y))
print(type(x),x)
y = int(y)
print(type(y),y)
y = float(y)
print(type(y),y)  