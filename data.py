# import ev3dev.ev3 as ev3
import time
import process as p

class usercolor:
	def __init__(self):
		self.password = 0
		self.money = 0
		self.trash = 0
		self.recycle = 0
		self.username = ''

def start():
	print("this is recycle system terminal\n", "1. create user\n 2.userdata\n 3. start system \n 4. end system \n")
	choice = int(input("Please select your input:"))

	switch(choice){
		case 1:
			coloru = str(input("color"))#color sensor
			exec(coloru + '= usercolor()')
			exec(coloru + ".username = str(input('enter your name:')")
			exec(coloru + ".password = str(input('enter your password:')"")
		case 2:
			userc = str(input("color"))#color sense card
			print("amount of currency", exec(userc + ".money"), "\n", "trash amount", exec(userc + ".trash"), "\n","recycle amount" ,exec(userc + ".recycle"))
		case 3:
			p.startsys()
		case 4:
			p.endsys()
	}
