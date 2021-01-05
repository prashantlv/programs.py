from array import *

arr = array ("i",[12321,32,232,122])
ln = len(arr)
for x in range(ln):
	sum=0
	temp=arr[x]
	if x<=ln:
	 	while temp>0:
	 		r=temp%10
			sum = sum*10+ r
			temp=temp//10
			if sum==arr[x]:
				print(sum)
			


