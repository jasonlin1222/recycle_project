import ev3dev.ev3 as ev3

class user:
	def __init__(self):
		self.password = 0
		self.money = 0
		self.trash = 0
		self.recycle = 0


def start():
	print("this is recycle system terminal\n", "1. create user\n 2.userdata\n 3. start system \n 4. end system \n")
	choice = int(input("Please select your input:"))
	if choice == 1:
		name = str(input('enter your name:'))
		exec(name + " = user()")
	elif choice == 2:
		username = str(input("enter your username:"))
		print(exec(username + ".money"), "\n", exec(username + ".trash"), "\n", exec(username + ".recycle" )
