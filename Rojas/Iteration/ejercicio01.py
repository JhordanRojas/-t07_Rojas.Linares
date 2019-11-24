import os
# Decodificador de texto secreto
#x : Bienvenido
#y : este mensaje es una prueba
#z : para verificar el programa
#w : listo!

sms_secreto=os.sys.argv[1]
#iterador
for word in sms_secreto:
    if word == "x":
        print("Bienvenido")
    if word == "y":
        print("este mensaje es una prueba")
    if word == "z":
        print("para verificar el programa")
    if word == "w":
        print("listo!")

#Fin_iterador
print("fin del bucle")
