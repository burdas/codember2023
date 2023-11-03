from collections import Counter
def decript(message: str):
    words = message.lower().split()
    result = ''
    for clave, valor in Counter(words).items():
        result += f"{clave}{valor}"
    return result

with open('D:\Proyectos\codember2023\CHALLENGE01\message_01.txt', 'r') as archivo:
    # Lee todo el contenido del archivo en un string
    contenido = archivo.read()

print(decript(contenido))