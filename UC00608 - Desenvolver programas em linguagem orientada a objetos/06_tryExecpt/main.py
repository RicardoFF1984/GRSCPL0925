lista = [1, 2, 3, 4]

print(lista[0])
# print(lista[10]) # -> IndexError

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])
# print(my_dict['f']) # -> keyError


num_in = "10"
print(int(num_in))

num_in = "Dez"
# print(int(num_in)) # -> ValueError

try:
    # print(lista[10])
    print(int(num_in))
except Exception:
    print("IndexError")

print("o codigo vai terminar")
