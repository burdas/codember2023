with open('.\\files.txt', 'r') as archivo:
    i = 0
    for line in archivo:
        [file, checksum] = line.strip().split("-")
        new_checksum = ''.join(caracter for caracter in file if file.count(caracter) == 1)
        if checksum == new_checksum:
            i+=1
        if i == 33:
            print(checksum)