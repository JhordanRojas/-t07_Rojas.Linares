import os

# Decodificar texto
# M = Se hace camino al andar
# N = Caminante, no hay camino
# P = El camino y nada mas
# Q = Caminante son tus huellas

mensaje=os.sys.argv[1]

for letter in mensaje:
    if letter == "M":
        print("Se hace camino al andar")
    if letter == "N":
        print("Caminante, no hay camino")
    if letter == "P":
        print("El camino y nada mas")
    if letter == "Q":
        print("Caminante son tus huellas")

#Fin_iterador
print("fin del bucle")
