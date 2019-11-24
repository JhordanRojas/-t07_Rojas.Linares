import os
#Descifrar informacion
#a: produccion y manufactura de la seda:
#b: disminucion de la produccioon de la seda en el siglo xx
#c: desarrolo de la tecnica de la seda:oriente medio y grecia
#d: italia y espana: importantes productores en la edad media
#e: china: actual primer productor

la_seda=os.sys.argv[1]
code=""

#iterador
for code in la_seda:
    if code == "a":
        print("Produccion y manufactura de la seda:")
    if code == "b":
        print("disminucion de la produccioon de la seda en el siglo xx")
    if code == "c":
        print("desarrolo de la tecnica de la seda:oriente medio y grecia ")
    if code == "d":
        print("Italia y Espana: importantes productores en la edad media")
    if code == "e":
        print("China: actual primer productor")

#Fin_iterador
print("fin del bucle")

