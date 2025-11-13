# list

lst = [1,2,3,4]
print(lst)

lst.append(5) # add no final

print(lst)

lst.insert(1,6) # add na pos indicada
print(lst)

lst.count(5) # conta num de vez q um valor se repete

lst.reverse() # devolve a lista invertida

lst.pop() # remove o ultimo

lst.pop(2) # remove o que estiver no idx indicado


lst = [1,4, 2,4,3,4]
lst.remove(4) # remove a 1 ocorrência valor indicado,

lst.sort() # ordena por ordem crescente

lst.sort(reverse=True)   # ordena por ordem decrescente


print(lst[2])

"""
obj:  pedir a utilizador 1000 num, colocar os num numa lista e devolver uma lista ordenada

opt1 - inserir os valores já ordenados - insert
ordem de inserção 1,2,10,15,13,7

[1]
[1,2]
[1,2,10]
[1,2,10, 15]
[1,2,10,13,15]
[1,2,7,10,13,15]
[1,2,3, 7,10,13,15]

opt2 -  inserir os valores no final  -append
     -  quando tiver todos os valores ordenar a lista  - sort

ordem de inserção 1,2,10,15,13,7
receber num
[1]
[1,2]
[1,2,10]
[1,2,10,15]
[1,2,10,15,13]
[1,2,10,15,13,7]
[1,2,10,15,13,7,3]

ordenar:


[1,2,3,7,10,13,15]

newval = 11

ver se val >= q new val - insert
[1,2,3,7,10,13,15]

"""

lst = [1,2,3,4]

lst.insert(9999999999,5)



print(lst)