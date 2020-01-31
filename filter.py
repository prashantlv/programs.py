# print evens from list

seq = [1,2,3,4,5,5,6,7,8]

def even(a):
	return a%2==0

num = list(filter(even,seq))	#filter(function,sequence)
print(num)

# using lambda 

print(list(filter(lambda a : a%2==0,seq)))

