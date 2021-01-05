list = [1,3,12,21,22]
n=4
def search(list,n):
	l,u = 0,len(list)-1
	while l <= u:
		mid = (l+u) // 2
		if list[mid] == n:
			return True
		else:
			if list[mid] < n:
				l = mid+1
			else:
				u = mid -1
	return False		

if search(list,n):
	print("found")
else:
	print("Not Found")	