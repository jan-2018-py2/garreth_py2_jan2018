class Animal(object):
	def __init__(self, name):
		self.health = 100
		self.name = name

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def get_killed_by_night_king(self):
		self.health = "dead"
		return self

	def display_health(self):
		print "**********"
		print "This animal's name is " + self.name + "."
		print "S/he has " + str(self.health) + " health."

	# def display_all(self):

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

dog = Dog("Rigby")
dog.walk().walk().run().pet().display_health()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 150

dragon = Dragon("Viserion")
dragon.get_killed_by_night_king().display_health()