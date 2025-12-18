"""
Crie uma class carro -> Done


instancie a class -> Done

mostre os seus atributos
----------------------

Alerter a class de forma a ser possível o carro acelarar

adicione um metodo para travar

adicione um metodo que calcule a distância que o carro andou
(pode receber a hora de inicio e a hora de fim, pode assumir que o carro andou com uma velocidade constante)
    garanta que a hora e uma str com o formato->  00:00  <- (sem usar o datetime)

"""


# todo - por fazer
# fixme - a dar erro, tem de ser revisto


class Carro:
    def __init__(self, marca: str, modelo: str, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor


carro1 = Carro('Ford', 'Mustang', "Preto")

# print(carro1.marca)
# print(carro1.modelo)
# print(carro1.cor)

print(f"o carro é um {carro1.marca} {carro1.modelo} {carro1.cor}")
