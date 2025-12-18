def teste(args):
    print(args)


def teste2(*args):
    print(args)


teste("Ola Mundo")
teste2("Ola Mundo", "Ola Mundo2")
tp = "Gonçalo", 2025, "ATEC"

teste2(*tp)


def soma(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


lista_nums = (1, 2, 5, 10)

print(soma(1, 4, 10))

print(soma(*lista_nums))

n1, n2, n3, n4 = lista_nums


def teste3(**kwargs):
    print(kwargs)


idx = "idx mais cool que a var"
foo = "var cool"

boo = 23141212

teste3(nome="valor1", telefone="valor2")

my_dict = {idx: foo, "telefone": boo}

teste3(**my_dict)
