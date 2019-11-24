import os
#suma de los n primero cuadrados perfectos
x=int(os.sys.argv[1])
y=int(os.sys.argv[2])

serie=0

while (x<y):
    serie+=x**2
    x+=1

#Fin_para
print("fin del bucle")
print("El valor de la serie de los 8 primeros cuadrados perfectos es:",serie)
