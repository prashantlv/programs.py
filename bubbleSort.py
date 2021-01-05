list = [4,5,2,2,1,18,9]

for i in range(len(list)-1,0,-1):
	for j in range(i): 
		if list[j] > list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]
		else:
			pass
print(list)	