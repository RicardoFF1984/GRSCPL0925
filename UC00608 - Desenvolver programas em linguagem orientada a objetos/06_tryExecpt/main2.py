try:
    num_in = "10"
    print(int(num_in))  # -> ValueError

except ValueError:  # corre quando há erros
    print("Oops! Something went wrong.")

else:  # corre quando não há erros
    print("a conversão correu bem")

finally:  # corre sempre 
    print("o programa vai terminar ")
