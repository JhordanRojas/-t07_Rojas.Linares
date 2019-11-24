import os
#suma de los cubos de los q primeros numeros naturales
p=int(os.sys.argv[1])
q=int(os.sys.argv[2])

valor_suma=0

while (p<=q):
    valor_suma+=p**3
    p+=1

#Fin_para
print("suma de los cubos de los 4 primeros numeros naturales es:", valor_suma)
print("fin del bucle")
