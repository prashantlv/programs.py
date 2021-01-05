square = []
for x in range(11):
	square.append(x*x)
print(square)


square = list(map(lambda x : x*x,range(11))) #lamda fun
print(square)	


square = [x*x for x in range(11)]		#list comprehenssion
print(square)

square = [x*x for x in range(11) if x%2==0] # filter can be given
print(square)