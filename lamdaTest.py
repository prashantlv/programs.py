lis = [1,3,2,5,6,8,9,5,4,3,4,3,4]

even = list(filter(lambda a : a%2==0,lis))
print(even)
print()

update = list(map(lambda b : b+2.0,even))
print(update)
