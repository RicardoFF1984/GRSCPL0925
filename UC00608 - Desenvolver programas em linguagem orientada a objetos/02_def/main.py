
# ola mundo, "1ª" func em python - 13\11\2025
def ola_mundo():
    print('ola mundo, "1ª" func em python')

def ola_mundo2():
    print("ola mundo, \"2ª\" func em python em 13\\11\\2025")

ola_mundo2()


def ola_mundo3():
   return "ola mundo, \"3ª\" func em python em 13\\11\\2025"


print(ola_mundo3())
my_msg = ola_mundo3()

#print(my_msg.split("\""))



def ola_mundo4(nome):

    return f"ola mundo, \"{nome}\""

print(ola_mundo4("Gonçalo"))

#type hint
def nova_func(cidade: str):

    print(f"nova func em python em {cidade}")


nova_func("Sintra")

nova_func(2025 +25)

var_a: str = "nome"

print(var_a)

var_a = "novo nome"

print(var_a)


var_a = 1234

print(var_a)


def soma(val1: int, val2: int) -> int:
    return val1 + val2


def subtracao(val1: int, val2: int) -> int:
    return val1 - val2



def soma2(val1: int = 4, val2: int = 5) -> int:
    return val1 + val2

# 127.0.0.1
def config_host(ip :str = "127.0.0.1", port :int = 8080 ):
    print(f"config_host em {ip}:{port}")

print(soma(4, 5))
print(soma2())


config_host("192.168.1.1", 3306)

config_host(ip="192.168.1.1", port=3306)

config_host(ip="127.0.0.1", port=3306)


config_host(port=3306, ip="192.168.1.81")

"""

8080 - servidor http local
80- http
3306 - mysql


"""
def config_host2(service:str = "http local", ip :str = "127.0.0.1", port :int = 8080 ):
    print(f"config {service} em {ip}:{port}")


config_host2(service="mysql", ip="127.0.0.1", port=3306)
config_host2("mysql", "127.0.0.1", 3306)
config_host2()
config_host2("http")
config_host2("http", ip="127.0.0.1", port=80)

