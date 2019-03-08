import ev3dev.ev3 as ev3
import time
import process as p
import pickle as pk
import os

col = ev3.ColorSensor('in1') #coop change
col.mode = 'COL-COLOR'
colors = ('unknown black blue green yellow red white brown'.split())

class usercolor:
	def __init__(self):
		self.password = ''
		self.money = 0
		self.trash = 0
		self.recycle = 0
		self.username = ''

def start():
	print("this is recycle system terminal\n", "1. create user\n 2.userdata\n 3. start system \n 4. end system \n")
	choice = int(input("Please select your input:"))

	if choice is 1:
		print("please scan your card...")
		time.sleep(5)
		coloru = colors[col.value()]
		while colors[col.value()] is unknown:
			try:
				print("error scaning card !!!")
				coloru = colors[col.value()]
			except KeyboardInterrupt:
				break
		if coloru is unknown:
			break
		else:
			exec(coloru + '= usercolor()')
			exec(coloru + ".username = str(input('enter your name:'))")
			exec(coloru + ".password = str(input('enter your password:'))")
	elif choice is 2:
		userc = colors[col.value()]
		try:
			print("amount of currency", exec(userc + ".money"), "\n", "trash amount", exec(userc + ".trash"), "\n","recycle amount" ,exec(userc + ".recycle"))
		except NameError:
			print("user does not exist !!!")
	elif choice is 3:
		p.startsys()
	elif choice is 4:
		p.endsys()