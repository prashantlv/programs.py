tel={'anam':15,'prashant':15,'preksha':21,'mahi':11}

# loop for retrieving elements from dictionary

for k,v in tel.items():
	print(k)


# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

for i,v in enumerate(tel):
	print(i,v)

# 	