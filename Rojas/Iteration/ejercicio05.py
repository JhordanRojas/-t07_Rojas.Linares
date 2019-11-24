import os
# Decodificar mensaje encriptado
# j = HOLA
# h = ELIGA IDIOMA:
# g = ESPANOL
# f = INGLES

text=os.sys.argv[1]
letra=""

#iterador
for letra in text:
    if letra == "j":
        print("HOLA")
    if letra == "h":
        print("ELIGA IDIOMA:")
    if letra == "g":
        print("ESPANOL")
    if letra == "f":
        print("INGLES")

#Fin_iterador
print("fin del bucle")
