#Funcion con argumentos variables, usando tuplas "*"
def funcion(cadena,repeticiones=2,*otros):
	print cadena*repeticiones
	
	for tupla in otros:
		print tupla*repeticiones

#Usando la funcion
print "\nUsando una funcion con argumentos variables, a traves de tuplas"
funcion('hola', 3, 'Python', 'C', 'C#', 'Java')