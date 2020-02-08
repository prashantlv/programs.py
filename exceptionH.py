a,b = 7,0

try:
	print(a/b)
except Exception :
	print("Exception handled")
print("Done")


a,b = 7,0

try:
	print(a/b)
except Exception as e :		# e is used as alias, any could be handled
	print("Exception {} handled ".format(e))
print("Done")

