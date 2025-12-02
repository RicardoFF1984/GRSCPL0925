import json

json_data = '[{"nome": "nome1", "idade": 30, "email": "nome1@mail.com"}, {"nome": "nome1", "idade": 30, "email": "nome1@mail.com"}]'

my_data = json.loads(json_data)

print(my_data[0])
