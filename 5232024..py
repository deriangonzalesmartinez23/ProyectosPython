
#Comparaciones Simples
EsMayor=10>5 #True , poque 10 es mayor que 5
EsIgual= 10==10#Truw , porque 10 es igual a 10
EsMenor=5<10 #True , porque 5 es menor que 10
EsDistinto=10 !=5 #True porque 10 no es igual a 5

#Operaciones logicas
EsVerdadera= True
EsFalso=False

#Logica Combinada

resultado_And=EsVerdadera and EsFalso # false
resultado_Or= EsVerdadera or EsFalso
resultado_NOT= not EsVerdadera

#Imprimir resultados
print("10 es mayor que 5", EsMayor)
print("10 es igual  10 ", EsIgual)
print("5 es menor que 10", EsMenor)
print("10 es distinto que 5", EsDistinto)


print("True AND False",resultado_And)
print("True OR False",resultado_Or)
print("NOT True ",resultado_NOT)
