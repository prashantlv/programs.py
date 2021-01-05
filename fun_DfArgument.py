class fun:
	def ask(self,prompt, retries = 3, reminder = 'Please try again !'):
		while  True:
			ok = input(prompt)
			if ok in ('y', 'Y', 'ye', 'Ye', 'Yes', 'yes', 'ya', 'yaa'):
				return True
			elif ok in ('n', 'N', 'no', 'No', 'Nope', 'nope', 'na', 'naa'):
				return False
			else:
				retries-=1
			if retries < 0:
				raise ValueError('invalid input')	
			print(reminder)

ob = fun()
ob.ask('Do you really want to quit?',2,'Type properly !')			