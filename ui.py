import ev3dev.ev3 as ev3
import time
import process as p
import pickle as pk
import os
import subprocess

#init
doorm = ev3.MediumMotor('outC')
assert doorm.connected
inm = ev3.LargeMotor('outB')
assert inm.connected
transm = ev3.LargeMotor('ouA')
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
colu = list()
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
		print("please scan your card...")
		time.sleep(5)

		coloru = colors[coldoor.value()]
		while colors[coldoor.value()] is unknown:
			try:
				print("error scaning card !!!")
				coloru = colors[coldoor.value()]
			except KeyboardInterrupt:
				break
		if coloru is not in user:
			user[coloru] = usercolor()
			user[coloru].username = input('enter your name')
			user[coloru].password = input('enter your password:')
		else:
			print("user already exist")
		# exec(coloru + '= usercolor()')
		# exec(coloru + ".username = str(input('enter your name:'))")
		# exec(coloru + ".password = str(input('enter your password:'))")
	elif choice is 2:
		userc = colors[coldoor.value()]
		try:
			print("amount of currency", user[userc].money , "\n", "trash amount", user[userc].trash, "\n","recycle amount" ,user[userc].recycle)
		except NameError:
			print("user does not exist !!!")
	elif choice is 3:
		subprocess.run("python3 system.py", shell = True)
	elif choice is 4:
		with open("userdata.txt", "w+") as file:
			pk.dump(user, file) # file arr init
			print("saving system.....")
			time.sleep(5)
