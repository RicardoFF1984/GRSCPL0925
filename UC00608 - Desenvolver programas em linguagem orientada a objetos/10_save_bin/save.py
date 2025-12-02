import pickle

users = [
    {
        "nome": "nome1",
        "idade": 30,
        "email": "nome1@mail.com"
    },
    {
        "nome": "nome2",
        "idade": 32,
        "email": "nome2@mail.com"
    },
    {
        "nome": "nome4",
        "idade": 34,
        "email": "nome4@mail.com"
    },
    {
        "nome": "nome3",
        "idade": 33,
        "email": "nome3@mail.com",
        "turma": "Turma"
    },

]

with open("users.grsc", "wb") as f:
    pickle.dump(users, f)
