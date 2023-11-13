def minicompiler(message: str):
    value = 0
    for character in message:
        if character == "#":
            value += 1
        elif character == "@":
            value -= 1
        elif character == "*":
            value *= value
        else:
            print(value,end="")
    print()

minicompiler("&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&")