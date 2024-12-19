# JSON format

JSOn = java Script Object Notation

supported in many languages

Not all Python types can be serialized in JSON
 for example - Datetime objects

In example script - Calculate average ride duration, by reading json logs

Note: 
```sh
json.loads(textline, object_pairs_hook=smth)
```
object_pairs_hook is an optional function that will be called with the result of any object literal decoded
with an ordered list of pairs. The return value of object_pairs_hook will be used instead of the dict. 
This feature can be used to implement custom decoders. If object_hook is also defined, the object_pairs_hook takes priority.


The object_pairs_hook parameter in the json.loads() method allows you to specify a function or callable 
that will process the key-value pairs of JSON objects as they are being decoded. 
Instead of converting JSON objects into a regular Python dictionary, this parameter lets you use a custom data structure or transformation.

The parameter receives the key-value pairs of a JSON object as a list of tuples (preserving the order) and applies the function you provide to transform the data.

Why Use object_pairs_hook?
To maintain the order of keys in a JSON object (dictionaries in Python prior to version 3.7 did not guarantee order).
To use a custom mapping type like collections.OrderedDict or a custom function for processing the key-value pairs.


Examples:
```python
import json
from collections import OrderedDict

# JSON string
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Decode JSON with object_pairs_hook
result = json.loads(json_string, object_pairs_hook=OrderedDict)

print("Result:", result)
print("Type:", type(result))
#Result: OrderedDict([('name', 'Alice'), ('age', 30), ('city', 'New York')])
#Type: <class 'collections.OrderedDict'>
```
Advanced Example:
```python
import json
# Custom function to transform key-value pairs
def custom_hook(pairs):
    return [f"{key}: {value}" for key, value in pairs]

# Decode JSON with custom object_pairs_hook
result = json.loads(json_string, object_pairs_hook=custom_hook)

print(result)
# ['name: Alice', 'age: 30', 'city: New York']
```