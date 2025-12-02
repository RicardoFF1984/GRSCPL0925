print("----------------.read()-----------------")

file = open("info.txt", "r")

print(file.read())

file.close()

print("---------------file.read() x 2 ------------------")

file = open("info.txt", "r")

print("----")
print(file.read())
print("----")
print(file.read())
print("----")

file.close()

print("---------------file.read(x)------------------")

file = open("info.txt", "r")

print(file.read(8), end="")
print(file.read(18), end="")
print(file.read(21), end="")
print(file.read(46), end="")
print(file.read(4), end="")
file.close()

print("---------------file.readline() e readline(x)------------------")

file = open("info.txt", "r")

print(file.readline())
print(file.readline())
print(file.readline())
print("----")
print(file.readline(440))

file.close()

print("------------- for line in file -------------------")

file = open("info.txt", "r")

for line in file:
    print(line)

file.close()

print("--------------------------------")
