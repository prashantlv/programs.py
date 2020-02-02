str = 'hello Geeks, we are Dev'

print(str)

for x in str:
	print(x.upper(), end= "")
print()
for x in str:
	print(x.lower(),end="")
print()

print("______________________")	

for i in str:
	print(i.strip(),end="")			# remove all spaces
print()
# for j in str:
# 	print(j.split(),end="")          split every character and make list separatly

print("length is :",len(str))		# including spaces and coma
