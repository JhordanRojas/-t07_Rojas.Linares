import os
#suma de las inversas de los n primeros numeros naturales
a=int(os.sys.argv[1])
n=int(os.sys.argv[2])

valor_serie=0

while (a<=n):
    valor_serie+=(1/a)
    a+=1


#Fin_para
print("el valor de la sumatoria de las inversas de los 10 primeros numeros naturales es:", valor_serie)
print("fin del bucle")
