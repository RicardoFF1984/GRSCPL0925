class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property  # criar um getter -> qd estao a ler
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter  # criar um setter -> qd estao a escrever a var, não ha  setter sem getter
    def idade(self, idade):
        if idade > 0 and idade < 100:
            self._idade = idade
        else:
            raise ValueError("Idade invalida")

    def funcCool(self):
        print(self.nome)
        print(self.idade)


class Aluno(Pessoa):  # Aluno seja uma Pessoa

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.turma = None

    def funcCool_Aluno(self):
        super().funcCool()


class A:  # independente
    pass


class B(A):  # B herda de A <- B seja B mas e verdade que B -> A
    pass


"""

Mesh 

inicio      -> no1
            -> no2
            -> no3 

"""
