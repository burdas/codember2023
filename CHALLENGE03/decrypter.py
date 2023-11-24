with open('D:\Proyectos\codember2023\CHALLENGE03\input.txt', 'r') as archivo:
    i = 0
    for line in archivo:
        min = int(line.split(":")[0].split(" ")[0].split("-")[0])
        max = int(line.split(":")[0].split(" ")[0].split("-")[1])
        letra = line.split(":")[0].split(" ")[1]
        password = line.split(":")[1].strip()
        if min > password.count(letra) or password.count(letra) > max:
            i += 1
        if i == 42:
            print(password)
            exit()