test = 1,2,3,2,4,'geeks','in','the','house.'		#one way of defining- separated by comas

print(test)

test1 = set('another')						#create set of charcter pf string								
test2 = set('problem')
print(test1)

#--------------------operations

print(test1 | test2)		# all the unique character set

print(test1-test2)			# as planned

print(test1 & test2)		# comman in both

print(test1 ^ test2)		# letters in test1 or test2 but not in bo
