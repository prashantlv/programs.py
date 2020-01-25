# list as stack

berry = ['hello',' !','geeks']

print(berry)

berry.append('.')
print(berry)

berry.insert(4,'lets do it')
print(berry)

berry.insert(4,'now what')		# insert at index and shift rest following
print(berry)

berry.append(2)
berry.append(3)
berry.append(4)
berry.append(5)
berry.append(3)			# insert at last	
print(berry)

berry.remove(3)			# remove first element maching
print(berry)

berry.pop()				# remove last element
print(berry)

berry.pop(7)			# remove at index
print(berry)

print(berry.index('geeks'))	# return the index of elelment

print(berry.index(2,3,7)) #  3 is start and 7 is end, thisis done to reduce search


berry.insert(8,3)
print(berry)
berry.append(2)

berry.insert(9,[1,2,3,4,5])
print(berry)

print(berry[9])

print(berry.count(2))	# returns no. of times element appear in list

print(berry)

print(berry[0:6])		#slicing 0-start 6-end index

print(berry[::-1])		# reverse through slicing

print(berry[0:6:2])		# jump by 2 in indexing

nums = [2,4,2,6,8,9,3]

print(nums[6:0:-1])     #  REVERSE


 # nums.clear will clear the list equivalent to del nums[:]

del nums[2:4]		# removed 2,6
print(nums)

print(nums.reverse()) # reverse element
