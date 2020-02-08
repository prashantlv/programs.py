list = []
n = int(input("Number of elements: "))
for i in range(n):
	list.append(input("Enter elements to append: "))
for i in range(n):
	print(list[i],end = " ")	