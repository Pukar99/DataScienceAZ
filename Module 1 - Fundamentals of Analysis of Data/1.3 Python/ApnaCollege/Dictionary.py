#Dictionary in Python
# A built in data type that lets us store a collection of data.
# They are unordered, changeable and indexed.
# They have keys and values.
# The keys should be unique.

dict = {"name":"John", "age":25, "city":"New York"}
print(dict)
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}
print(type(dict))
# Output: <class 'dict'>

print(dict["name"])
# Output: John

info = {"key":"value", "name":"John", "age":25, "city":"New York", "marks":[45, 78.5, 86, 77, 90]}
print(info)
# Output: {'key': 'value', 'name': 'John', 'age': 25, 'city': 'New York', 'marks': [45, 78.5, 86, 77, 90]}
print(info["marks"])
# Output: [45, 78.5, 86, 77, 90]


info["name"] = "pukar"
print(info)
# Output: {'key': 'value', 'name': 'pukar', 'age': 25, 'city': 'New York', 'marks': [45, 78.5, 86
# , 77, 90

#Nested Diccitionary
info = {"key":"value", "name":"John", "age":25, "city":"New York", "marks":[45, 78.5, 86, 77, 90], "student":{"name":"John", "age":25, "city":"New York"}}
print(info["student"])
# Output: {'name': 'John', 'age': 25, 'city': 'New York'}


#Dictionary Methods
dict = {"name":"John", "age":25, "city":"New York"}
print(dict.keys())
# Output: dict_keys(['name', 'age', 'city'])

print(dict.values())
# Output: dict_values(['John', 25, 'New York'])

print(dict.items())
# Output: dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])

dict.pop("age")
print(dict)
# Output: {'name': 'John', 'city': 'New York'}

print(list(dict))
# Output: ['name', 'city']

print(dict.get("ram"))
# Output: None

print(dict.get("name"))
# Output: John

dict.clear()
# Output: {}

