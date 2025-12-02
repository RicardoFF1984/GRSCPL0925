import json

users = [
    {
        "nome": "nome1",
        "idade": 30,
        "email": "nome1@mail.com"
    },
    {
        "nome": "nome1",
        "idade": 30,
        "email": "nome1@mail.com"
    },

]

json_data = json.dumps(users)
print(json_data)
