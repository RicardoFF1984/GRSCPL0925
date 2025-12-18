"""

Metodo -> função dentro de uma class

"""


class Contacto:
    def __init__(self, nome: str, email: str, telefone: str):
        print("objeto inicilizado ")
        # print("criar uma instancia de contato")
        self.nome = nome
        print(f"criar uma instancia do contato com nome: {nome}")
        self.mail = email
        self.telefone = telefone

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone
