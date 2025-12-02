"""

ler e escrever em ficheiros de txt e bin


r - read
a - append
w - write
x - create


------------

t - txt
b - bin

"""

num = 9

file = open("info.txt", "w")

file.write(f"Hello World {num}\n")
file.write(f"Hello World {num}\n")
file.write(f"Hello World {num}\n")
file.write(f"Hello World {num}\n")

file.close()

num = 10

file = open("info.txt", "w")

file.close()
