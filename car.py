class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax
		self.tax()
		self.display_all()

	def tax(self):
		if self.price >= 10000:
			self.tax = ".15"
		else:
			self.tax = ".12"

	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax

car1 = Car(5000, "75mph", "full tank", "18mpg")
car2 = Car(17000, "105mph", "three quarters tank", "35mpg")
car3 = Car(300, "45mph", "empty tank", "13mpg")
car4 = Car(50000, "100mph", "half full tank", "75mpg")


