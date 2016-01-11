class Coche:

	def __init__ (self, galosina):
		self.gasolina = galosina
		print "Tenemos ", self.gasolina, " litros"

	def conducir(self):
		if self.gasolina > 0:
			self.gasolina -=1
			print "Quedan ", self.gasolina, " litros"
		else:
		 	print "No se mueve"

	def arrancar(self):
		if self.gasolina > 0:
			print "Arranca"
		else:
			print "Ya no hay galosina" 

car = Coche(10)

car.arrancar()

car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 
car.conducir() 

