#  Heterogeneous
tup = 12,34,56,'hello'		#one way of defining 
print(tup)

tupr = tup,'geeks','nested tuple' #nested tuples
print(tupr)

print(tup[2])	

print(tup[1:3])		#slicing

#	tup[0] = 21    not possible, tuples are immutable

empty_tup = ()
print(empty_tup)