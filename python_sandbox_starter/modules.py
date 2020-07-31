# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core modules
import datetime
from datetime import date #to import only date
import time
from time import time

#pip module
from camelcase import CamelCase

#import custom module

import validator
from validator import validate_email

today = date.today()
print(today)

timestamp = time()
print(timestamp)

# pip is the package manager of python
# to install something with pip type pip install package name
# When using a environment you can do pipenv to install locally to an environment

c = CamelCase()
print(c.hump('hello world'))
email = 'test1test.com'
if(validate_email(email)):
    print('valid email')
else:
    print('in-valid email')

