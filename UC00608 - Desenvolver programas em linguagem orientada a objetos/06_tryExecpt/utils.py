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
        msg_erro: str = "o valor introduzido não e numérico.",
        new_line: bool = True):
    while True:
        try:
            num = _type(input(prompt))
        except ValueError:
            print(msg_erro, end=f"{"\n" if new_line else ""}")
        else:
            return num
