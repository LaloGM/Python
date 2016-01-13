class Humano:
	def __init__(self,name,old):
		self.nombre = name
		self.edad = old

class Ingeniero(Humano):
	def Carrera(self,ingenieria):
		self.tipo = ingenieria

	def presentacion1(self):
		print 'Hola\n'
		print 'Me llamo ', self.nombre
		print '\nTengo ', self.edad, ' years'
		print '\nSoy ingeniero en ', self.tipo

class Cientifico(Humano):
	def Ciencia(self, rama_ciencia):
		self.Scien = rama_ciencia

	def presentacion2(self):
		print 'Hola'
		print '\nMe llamo ', self.nombre
		print '\nTengo ', self.edad, ' years' 
		print '\nSoy cientifico en ', self.Scien

#Creacion de los objetos
Tessla = Ingeniero('Nikola Tessla', 100)
Gauss = Cientifico('Gauss',300)

#Implementacion de los metodos para cada tipo de objeto
Tessla.Carrera('Ingenieria Electronica')
Tessla.presentacion1()

print '____________________________________________________________________\n'

Gauss.Ciencia('Matematicas')
Gauss.presentacion2()
