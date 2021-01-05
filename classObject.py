class room:
	def furniture(self):
		items = ['bed','chair','table','almirah']
		print(items)

rm1 = room()
rm2 = room()		# room() is constructor and rm is object

room.furniture(rm1)

#note : if we remove self from method then room.furniture() will be enough

rm1.furniture()		# behine the scene furniture will take rm1 as perameter