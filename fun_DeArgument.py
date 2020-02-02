i = 2
def fun(arg=i):
	print(arg)
i = 3
fun(i)		# print 2 if i not passed here, coz argument assign at defination time