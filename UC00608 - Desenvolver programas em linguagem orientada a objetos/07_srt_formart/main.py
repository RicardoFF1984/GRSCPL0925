nome = "Gonçalo"
ano = 2025

print("Hello World" + " " + nome + " em " + str(ano))

print(f"Ola mundo {nome} em {ano}")  # > py 3.6

print("Ola mundo antigo {} em {}".format(nome, ano))  # > py 3.6

print("-----------------------------")

print(f":< {nome:<20}")
print(f":^ {nome:^20}")
print(f":> {nome:>20}")

print("-----------------------------")

print(":> -> {:>20}".format(nome))

print("-----------------------------")

num = 1000000

print(f"{num}")
print(f"{num:+}")
print(f"{num:-}")

print(f"{num:,}")
print(f"{num:_}")

print(f"{num:e}")
print(f"{num:E}")

print(f"{num:g}")

print("-------------- num = 255 ---------------")
num = 255
print(f"{num:d}")

resp = f"{num:b}"
print(resp)

print(f"{num:o}")

print(f"{num:x}")
print(f"{num:X}")

print("-------------- num = \"0xFF\" ---------------")
num = "0xFF"  # <- hexa
num = int(num, 16)

print(f"{num:d}")

resp = f"{num:b}"
print(resp)

print(f"{num:o}")

print(f"{num:x}")
print(f"{num:X}")

print("-------------- num = \"0oFF\" ---------------")
num = "0o55"  # <- octal
num = int(num, 8)

print(f"{num:d}")

resp = f"{num:b}"
print(resp)

print(f"{num:o}")

print(f"{num:x}")
print(f"{num:X}")

"""

int() -> base 10
int(, 8) -> base 8 (Octal)
int(, 16) -> base 16 (Hex)) 

"""

print("-------------- num = 0xFF ---------------")
num = 0xFF  # <- hexa
print(type(num))

print(f"direto - {num}")
print(f"{num:d}")

resp = f"{num:b}"
print(resp)

print(f"{num:o}")

print(f"{num:x}")
print(f"{num:X}")

print("-------------- num = 0oFF ---------------")
num = 0o41  # <- hexa
print(type(num))

print(f"direto - {num}")
print(f"{num:d}")

resp = f"{num:b}"
print(resp)

print(f"{num:o}")

print(f"{num:x}")
print(f"{num:X}")

print("-----------------------------")

i = 86

print(f"{i:c}")  # -> converter para tabelas ascii

# i = "V"
# print(f"{i:d}") # -> erro ValueError: Unknown format code 'n' for object of type 'str

print("-----------------------------")

i = 0.25
print(f"{i}")
print(f"{i:.0%}")
print(f"{i:.2%}")

print("-----------------------------")

i = 1.158123

print(f"{i:.2f}")
