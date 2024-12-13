# named tuple
Type is presented inside Collections module

namedtuple( typename, field_names)
 - typename - the name of the namedtuple
 - field names - the list of attributes stored in the namedtuple

```
# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Tom', '29', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
```