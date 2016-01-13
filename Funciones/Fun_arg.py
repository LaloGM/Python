#Funcion utilizando argumentos
def Suma1(a,b):
	print a + b

#Funcion utilizando valores por default
def Suma2(a=0,b=0):
	print a + b

#Usando las funciones creadas
print '\nFuncion con argumentos dados: 2,3'
Suma1(2,3)

print '\n____________________________________________________________________________'

print '\nFuncion con argumentos default'
Suma2()
