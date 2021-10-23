from json import JSONEncoder
import json


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("neo", 22)

# dumping a custom object(method 1)


def encode_user_to_json(obj):
    if isinstance(obj, User):
        return{"name": obj.name, "age": obj.age, user.__class__.__name__: True}
    else:
        raise TypeError("This is not and object of type User")

def decode_json_to_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


# dumping a custom obj(method 2)


class UserEncoder(JSONEncoder):

    def default(self, obj):
        if(isinstance(obj, User)):
            return{"name": obj.name,"age": obj.age, object.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


# userJSON = json.dumps(user, indent=4, default=encode_user_to_json)
# userJSON = json.dumps(user, indent=4, cls=UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

#decodes it back
user = json.loads(userJSON, object_hook=decode_json_to_user)
print(user.name)
