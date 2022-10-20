
file = open("devices.txt", "r")

for line  in file:
    line = line.strip()

    opc = input('¿Qué dispositivo estas buscando? ')
    if opc in line:
        print(line)
    else: print("Dispositivo no encontrado")

file.close()