def main():
	string = input()
	flag=0
	for letter in string:
		if letter.isupper():
			flag+=1
		else:
			flag-=1
	if flag > 0:
		return string.upper()
	else:
		return string.lower()
if __name__=='__main__':
	print(main())
