# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#sample JSON

UserJson = '{"First name": "JOHN", "Last name":"Doe","Age":30}'

#parse to dict

user = json.loads(UserJson)
print(user)
print(type(user))

car = {'make':'Ford','model':'Mustang','year':'1970'}

carJSON = json.dumps(car)

print(carJSON)