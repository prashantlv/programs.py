nums = [1,2,4,5,6,6,7,8,8,4]

# for i in nums:
# 	print(i)

itr = iter(nums)	# iter method is used to create iterator of list

for i in nums:
	print(itr.__next__())