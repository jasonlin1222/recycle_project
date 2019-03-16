import ev3dev.ev3 as ev3
import time
import pickle as pk
import os
import re

#init
doorm = ev3.MediumMotor('outC')
assert doorm.connected
inm = ev3.LargeMotor('outB')
assert inm.connected
transm = ev3.LargeMotor('outA')
assert transm.connected
coldoor = ev3.ColorSensor('in2') #coop port
assert coldoor.connected
ts = ev3.TouchSensor('in3') #coop port
assert ts.connected
colin = ev3.ColorSensor('in1')
assert colin.connected
coldoor.mode = 'COL-COLOR'
colin.mode = 'COL-COLOR'
colors = ('unknown black blue green yellow red white brown'.split())
user = dict()
#init end
class usercolor:
	def __init__(self):
		self.password = ''
		self.money = 0
		self.trash = 0
		self.recycle = 0
		self.username = ''

def start():
	print("this is recycle system terminal\n", "1. create user\n 2. userdata\n 3. start system \n 4.save data \n")
	choice = int(input("Please select your input(1 ~ 4):"))

	if choice is 1:
		for i in range(1,6):
			print("please scan your card", '.' * i, end = "\r")
			time.sleep(1)
		coloru = colors[coldoor.value()]
		while coloru == "unknown":
			try:
				print("error scaning card !!!", end = "\r")
				time.sleep(5)
				print("                      ", end = "\r")
				coloru = colors[coldoor.value()]
			except KeyboardInterrupt:
				break
		if coloru not in user:
			user[coloru] = usercolor()
			user[coloru].username = input('enter your name: ')
			user[coloru].password = input('enter your password: ')
		else:
			print("user already exist")
		# exec(coloru + '= usercolor()')
		# exec(coloru + ".username = str(input('enter your name:'))")
		# exec(coloru + ".password = str(input('enter your password:'))")
							# exec use previous
	elif choice is 2:
		userc = colors[coldoor.value()]
		while userc == "unknown":
			try:
				print("error scaning card !!!", end = "\r")
				time.sleep(5)
				print("                      ", end = "\r")
				userc = colors[coldoor.value()]
			except KeyboardInterrupt:
				break
		try:
			print("amount of currency", user[userc].money , "\n", "trash amount", user[userc].trash, "\n","recycle amount" ,user[userc].recycle)
		except KeyError:
			print("user does not exist !!!")
		time.sleep(5)
	elif choice is 3:
		os.system("python3 system.py")
	elif choice is 4:
		with open("userdata.txt", "wb+") as file:
			pk.dump(user, file) # file arr init
			for i in range(1,6):
				print("saving system", '.' * i, end = "\r")
				time.sleep(1)
		exit(0)
