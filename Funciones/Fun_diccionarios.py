#Utilizando funciones con argumentos variables a travez de diccionarios
def funcion(repeticiones,cadena,**diccionarios):
	print cadena*repeticiones
	print diccionarios['cadenaextra1']*repeticiones
	print diccionarios['cadenaextra2']*repeticiones
	print diccionarios['cadenaextra3']*repeticiones

#Usando la funcion
print '\nFuncion con argumentos variables usando diccionarios'
funcion(3,'Python',cadenaextra1='C#',cadenaextra2='Java',cadenaextra3='Android')