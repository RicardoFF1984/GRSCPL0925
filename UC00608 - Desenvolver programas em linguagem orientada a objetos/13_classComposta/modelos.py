class Contacto:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return "isto é um contacto"

    def __repr__(self):
        return str(self)


class AgendaContacto:
    def __init__(self):
        self.lista_contactos: list[Contacto] = []

    """
    def adicionar_contacto(self, contacto):
        pass

    def adicionar_contacto(self, nome:str, telefone:str, email:str):
        pass
    """

    def adicionar_contacto(self, nome: str = None,
                           telefone: str = None,
                           email: str = None,
                           contacto: Contacto = None):
        # validar campos
        if type(contacto) == Contacto:
            self.lista_contactos.append(contacto)
        else:
            raise Exception('Contacto invalido')

        if type(nome) == str and type(telefone) == str and type(email) == str:
            # opt 2
            # ct = Contacto(nome, telefone, email)
            # self.lista_contactos.append(ct)

            # opt 2
            self.lista_contactos.append(Contacto(nome, telefone, email))

    def excluir_contacto(self):
        pass

    def pesquisar_contacto(self, nome: str) -> list[Contacto]:

        pass

    def contacto_duplicado(self) -> bool:
        pass
