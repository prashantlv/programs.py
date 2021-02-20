def main(a):
	count = 0
	if a > 5:
		count = count + a // 5
		a = a%5
	elif a > 4:
		count = count + a // 4
		a = a%4
	elif a > 3:
		count = count + a // 3
		a = a%3
	elif a == 2:
		count += 1
		a -= 2
	else:
		count += 1				
	print(count)

if __name__ == '__main__':
	x = int(input())
	main(x)

