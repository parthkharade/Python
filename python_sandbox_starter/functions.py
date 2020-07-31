# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#create a function 
def hello(name):
    print(f'Hello {name}')

#hello('Parth')

#Retuning values from a function

def getSum(num1, num2):
    S = num1+num2       #local variables
    return S

Sum = getSum(3,4)
print(Sum)


# A lambda function is a small anonymous function.


# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2

Sum = getSum(10,3)
print(Sum)

#If there are functions with the same name than the later will always over-ride the former.

 