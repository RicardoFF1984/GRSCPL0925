nomes = [
    "Miguel", "Inês", "Tiago", "Sofia", "João",
    "Mariana", "Diogo", "Beatriz", "Rodrigo", "Matilde",
    "Miguel", "Sofia", "João", "Inês", "Tiago",
    "Leonor", "Tomás", "Carolina", "Afonso", "Madalena",
    "Rafael", "Lara", "Henrique", "Francisca", "Guilherme",
    "Rodrigo", "Beatriz", "Miguel", "Ana", "Catarina",
    "Pedro", "Martim", "Vasco", "Miguel", "Sofia",
    "João", "Mariana", "Diogo", "Matilde", "Leonor",
    "Tomás", "Rafael", "Inês", "Francisca", "Lara",
    "Ana", "Catarina", "Pedro", "Guilherme", "Tiago"
]
print(len(nomes))

# print(nomes.__len__())

print(nomes[4])


print(nomes[4:10])

print(nomes[4:20:5])


print(nomes[-1]) # idx negativo fim

print(nomes[::-1]) # le do final para o inico

print(nomes[-5:-1])

print(nomes[1:-45])

print(nomes[1:5])


for idx, nome in enumerate(nomes):
    print(f"idx:{idx}, nome:{nome}")

# nova_lista = [exp for item in list if condição]
nova_lista = [elm for elm in nomes]
print(nova_lista)

nova_lista = [0 for elm in nomes]
print(nova_lista)

nova_lista = [elm for elm in nomes if elm.endswith("a")]
print(nova_lista)

nova_lista = [(elm, idx) for idx, elm in enumerate(nomes) if elm.endswith("a")]
print(nova_lista)

print(nomes)
print(nova_lista)


"""
1 - tendo uma lista de nomes2, crie uma nova lista com o tamanho de todos os nomes

2 - tendo uma lista de nomes2, crie uma nova lista com o tamanho de todos os começados por A

3 - tendo uma lista de nomes2, crie uma nova lista com o todos os nomes com um numero par de chars 

4 - tendo uma lista de nomes2, crie uma nova lista com o todos os nomes com um numero impar de chars, 
    os nomes devem estar invetidos, indique tambem o numero de letras e o index original do nome, 
    use o formato (nome, size, idx)
    
    
    Inês -> sênI
    
    Ana -> anA

"""

nomes2 = [
    "Miguel", "Inês", "Tiago", "Sofia", "João",
    "Mariana", "Diogo", "Beatriz", "Rodrigo", "Matilde",
    "Miguel", "Sofia", "João", "Inês", "Tiago",
    "Leonor", "Tomás", "Carolina", "Afonso", "Madalena",
    "Rafael", "Lara", "Henrique", "Francisca", "Guilherme",
    "Rodrigo", "Beatriz", "Miguel", "Ana", "Catarina",
    "Pedro", "Martim", "Vasco", "Miguel", "Sofia",
    "João", "Mariana", "Diogo", "Matilde", "Leonor",
    "Tomás", "Rafael", "Inês", "Francisca", "Lara",
    "Ana", "Catarina", "Pedro", "Guilherme", "Tiago"
]