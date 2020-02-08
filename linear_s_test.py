list = [2,3,4,5,5,6,6,6]
n=5
def search(list,n):
	for i in range(len(list)):
		if list[i] == n:
			print("h ",i+1," p ")
			break
	else:
		print("Ni milra")
search(list,n)			

				