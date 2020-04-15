import json

userJson = '{"firstName":"John", "lastName":"Doe", "age":30}'

user = json.loads(userJson)

print(user)

print(user["firstName"])

car = {'name':'ferarri', 'passenger':4}

carJson = json.dumps(car)

print(carJson)