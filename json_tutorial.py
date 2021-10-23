import json

# dict to conv to json obj(serialization)
person = {"name": "james", "age": 30, "city": "New york",
          "isSmart": True, "titles": ["coder", "investor", "engineer"]}

personJson = json.dumps(person, indent=4)    # conv to json obj
# print(personJson)

# dump to file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

# deserialization(conv json obj to py)
person = json.loads(personJson)
print(person)


# reads json obj file as python obj
with open("person.json", "r") as file:
    person = json.load(file)
    print(person)