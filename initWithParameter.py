class room:

	def __init__(self,wall,roof):
		self.wall = wall
		self.roof = roof
		
	def fun(self):
		print(self.wall,"  ",self.roof)		# if not self then: ErrorName- global name 'wall' is not defined
ob1 = room("offWhite","White")
ob2 = room("Pink","Red")

ob1.fun()
ob2.fun()

# it looks like we are passing two and accepting 3 arguments but indirectly we are passing ob to self		