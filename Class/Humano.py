#Declaracion de la clase Humano
class Humano:
	def __init__(self,old = 0,name='No body',pais='No body'):
		self.edad = old
		self.nombre = name
		self.nacionalidad = pais

	def Accion1(self):
		print '\n'
		print 'Me llamo ', self.nombre, 'tengo ', self.edad, " years y soy de ", self.nacionalidad

	def Accion2(self,ocupacion='No body'):
		print "Soy ", ocupacion

#Creacion de objetos de la clase HUmano
Einstein = Humano(100,'Albert Einstein','Alemania')
Newton = Humano(200,'Sir. Issac Newton','Inglaterra')
Invisible = Humano()

#Uso de los metodos
Einstein.Accion1()
Einstein.Accion2('Fisico')

Newton.Accion1()
Newton.Accion2('Fisico y matematico')

Invisible.Accion1()
Invisible.Accion2()
