def check(w):

	li = []
	for i in range(2,w,2):
		for j in range(2,w,2):
			if i + j == w:
				li.append('Y')	
			else:
				li.append('N')
	return li			

def main():
	w = int(input())
	li = check(w)
	if 'Y' in li:
		print('YES')
	else:
		print('NO')	
	
if __name__ == '__main__':
	main()				