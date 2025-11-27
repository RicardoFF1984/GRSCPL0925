from utils import safe_input

num = safe_input(int,
                 "Enter a number: ",
                 "o valor introduzido não e numérico.")
print(num)

num = safe_input(str, "Enter a string: ", "o valor introduzido não e str.")
print(num)

num = safe_input("float", "Enter a float: ", "o valor introduzido não e float.")
print(num)
