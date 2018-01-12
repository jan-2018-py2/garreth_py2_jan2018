class Bike(object):
    def __init__(self, price, max_speed):
    	self.price = price
    	self.max_speed = max_speed
    	self.miles = 0

    def displayInfo(self):
    	print self.price, self.max_speed, self.miles
    	return self

    def ride(self):
    	self.miles += 10
    	print "Riding", self.miles
    	return self

    def reverse(self):
    	self.miles -=5
    	print "Reversing", self.miles
    	return self

bike1 = Bike(200, "15mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(300, "25mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(1000, "35mph")
bike3.reverse().reverse().reverse().displayInfo()