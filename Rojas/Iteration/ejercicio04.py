import os
#decodificar texto informativo
#1:A partir del metro-patron,de jean-baptiste, esta unidad de medida alcanzo gran aceptacion
#2:El metro fue impuesto como unidad de medida durante la revolucion francesa
#3:El metro-patron es actualmente una pieza de museo
#4:El metro es un diezmillonesima parte del cuarto del meridiano terreste

metro=os.sys.argv[1]
number="" 

#iterador
for number in metro:
    if number == "1":
        print("A partir del metro-patron,de jean-baptiste, esta unidad de medida alcanzo gran aceptacion")
    if number == "2":
        print("El metro fue impuesto como unidad de medida durante la revolucion francesa")
    if number == "3":
        print("El metro-patron es actualmente una pieza de museo")
    if number == "4":
        print("El metro es un diezmillonesima parte del cuarto del meridiano terreste")
        
#Fin_iterador
print("fin del bucle")
