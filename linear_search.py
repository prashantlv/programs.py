list = [1,3,5,7,8]
n= 6
index = -1
def search(list,n):
	i=0
	while i < len(list):
		if list[i] == n:
			globals()['index'] = i
			return True
		i += 1
	return False

if search(list,n):
	print("Found at ",index+1)
else:
	print("Ni mila")	
