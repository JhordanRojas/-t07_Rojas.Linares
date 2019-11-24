import os
#suma de los numeros impares naturales hasta n
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])

sumatoria=0

while (m<n):
    sumatoria+=m
    m+=2

#Fin_para
print("El valor de la sumatoria de los numeros impares hasta 22 es",sumatoria)
print("fin del bucle")
