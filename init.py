class room:
	def function(self):
		print("Function")

	def __init__(self):
		print("init")
ob = room()		# __init__() is called everytime when object is created
ob.function()	