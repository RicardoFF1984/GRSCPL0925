from utils import safe_input

num = safe_input(int, "Enter a number: ", "")
print(num)

num = safe_input(str, "Enter a string: ", "")
print(num)

num = safe_input(float, "Enter a float: ", "")
print(num)
