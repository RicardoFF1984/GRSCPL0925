"""
S1
tipos de dados
var
in/out
condições
range
loops

def

S2
list
dict
set


"""


"""

tidos de dados

int
float
str (string)
bool - T/F


−2147483648  a 2147483648 <- int 32

-9223372036854775808 a 9223372036854775807 <- int 64
"""


num = 9_223_372_036_854_775_807
num2 = 9223372036854775807

print(num-num2)
#print(((n
#
# um*num2)*(num*num2))*((num*num2)*(num*num2)))

nome = "Gonçalo"
print(nome)
nome = 12
print(nome)


# in/out


nome = input("Digite seu nome: ")
print(nome)

idade = float(input("Digite seu idade: "))
print(idade)

idade2 = input("Digite seu idade: ")

if idade2.isnumeric():
    print("A idade deve ser um valor inteiro")
    idade2 = int(idade2)
else:
    idade2 = -1

print(idade2)

v1 = 10
v2 = 20

soma = v1 + v2

# Condições

#
# Faça um programa que receba 2 números e diga qual o maior
#


num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"o maior e {num1}")
else:
    print(f"o maior e {num2}")


#
# Faça um programa que receba 2 números e diga qual o maior, se forem iguais indique que são iguais
#

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"o maior e {num1}")
elif num2 > num1:
    print(f"o maior e {num2}")
else:
    print(f"os num são iguais")



#
# Faça um programa que receba uma idade, indique se a pessoa e Criança (0-12), teen(12-18), adulto (+18).
# se a idade for negativa indique que a idade e invalida
#





#
# Faça um programa que receba uma um número 1-12 e indique o mes correspondente
# 1 - Jan
# 2 - Fev
# ...
# 12 - Dez
#

"""
Comentario 
multi
linha
"""

"""
Crie o menu e peça a opção do utilizador 

######### Menu ########
# opt1              1 #
# opt2              2 #
# opt3              4 #
# opt4              5 #
#######################
opção: 

"""


# loops

# for

# while