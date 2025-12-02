import pickle

file_name = "users.grsc"

with open("users.grsc", "rb") as f:
    dados = pickle.load(f)

for d in dados:
    print(d)
