str1 = str(input())
str2 = str(input())

def reverse(s):
	str = ''
	for i in s:
		str = i + str
	return str

if __name__ == '__main__':
	str1 = reverse(str1)
	if str1 == str2:
		print('YES')
	else:
		print('NO')	