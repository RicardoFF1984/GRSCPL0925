"""def input_int(
        prompt,
        msg_erro="o valor introduzido não e numérico.",
        new_line=True):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print(msg_erro, end=f"{"\n" if new_line else ""}")
        else:
            return num
"""


def safe_input(
        _type: type,
        prompt: str,
        msg_erro: str = "",
        new_line: bool = True):
    # garantir que os param da func tem os tipos corretos -> ifs, type()

    # garantir que _type e um  type
    # garantir que prompt e uma str
    # garantir que msg_erro e uma str
    # garantir que new_line e um bool

    if not isinstance(_type, type):
        raise Exception(f"O primeiro parâmetro deve ser do tipo: {type(_type).__name__}")

    if not isinstance(prompt, str):
        raise Exception(f"O prompt deve ser do tipo string: {type(prompt).__name__}")

    if not isinstance(msg_erro, str):
        raise Exception(f"A mensagem de erro deve ser: {type(msg_erro).__name__}")

    if not isinstance(new_line, bool):
        raise Exception(f"O new_line deve ser booleano: {type(new_line).__name__}")

    while True:
        try:
            num = _type(input(prompt))
        except ValueError:
            print(msg_erro, end=f"{"\n" if new_line else ""}")
        else:
            return num
