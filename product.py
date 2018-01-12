# Garreth Broesche, Python fundamentals assignment "Product," for Coding Dojo, January 2018.

class Product(object):

	def __init__(self, price, item_name, weight, brand, status="for sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = status

	def sell(self):
		self.status = "sold"
		return self

	def return_item(self, return_reason, open_box):

		if return_reason == "defective":
			self.status = "defective"
			self.price = 0
			return self

		if open_box == False:
			self.status = "for sale"
			return self

		elif open_box == True:
			self.status = "used"
			self.price = self.price * .80
			return self

	def display_all(self):
		print "****", self.item_name, "****"
		print "Brand:", self.brand
		print "Price: $", self.price
		print "weight:", self.weight
		print "status:", self.status

dress_shoes = Product(120.99, "Fancy dress shoes", "1 lb 8 oz", "Gucci", "new")
dress_shoes.display_all()

dress_shoes.sell()
dress_shoes.display_all()

dress_shoes.return_item("too small", True)
dress_shoes.display_all()

