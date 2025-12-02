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

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)
