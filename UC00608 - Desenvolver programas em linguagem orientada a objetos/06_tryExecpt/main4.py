def teste(i: int):
    if not isinstance(i, int):  # boas praticas
        raise Exception(f"a param i dever ser do tipo int e não {type(i).__name__}")  # melhor msg
    print(i)


teste(2)

teste("dad")
