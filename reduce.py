from functools import reduce 		# need to import to use reduce

seq = [1,2,3,4,6,7,8,9,5,4,3]

num = reduce(lambda a,b : a+b,seq) 		# return number so no need to make list
print(num)				# add all values