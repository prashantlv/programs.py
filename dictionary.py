#set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}

# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary;
# this is also the way dictionaries are written on output.


tel ={'prashant': 15,'anam': 04}

print(tel)

print(tel['anam'])		# return the value of key anam

tel['preksha'] = 21		# add new entry

print(tel)

del tel['preksha']		# delete entry

print(tel)

sorted(tel)		#sort 

print(tel)

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

test = {x:x*x for x in range(2,11)}
print(test)

