import ev3dev.ev3 as ev3
import time
import process as p
import pickle as pk
import os

#init
doorm = ev3.MediumMotor('outC')
inm = ev3.LargeMotor('outB')
transm = ev3.LargeMotor('ouA')
coldoor = ev3.ColorSensor('in2') assert coldoor.connected #coop port
ts = ev3.TouchSensor('in3') assert ts.connected #coop port 
colin = ev3.ColorSensor('in1') assert colin.connected
coldoor.mode = 'COL-COLOR'
colin.mode = 'COL-COLOR'
colors = ('unknown black blue green yellow red white brown'.split())
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
		if coloru is unknown:
			break
		else:
			exec(coloru + '= usercolor()')
			exec(coloru + ".username = str(input('enter your name:'))")
			exec(coloru + ".password = str(input('enter your password:'))")
	elif choice is 2:
		userc = colors[coldoor.value()]
		try:
			print("amount of currency", exec(userc + ".money"), "\n", "trash amount", exec(userc + ".trash"), "\n","recycle amount" ,exec(userc + ".recycle"))
		except NameError:
			print("user does not exist !!!")
	elif choice is 3:
		os.system("python3 system.py")
	elif choice is 4:
		with open("userdata.txt", "w+") as file:
		for i in range(len(i.arr))
			pk.dump(, file) # file arr init
		 print("saving system.....")
		time.sleep(5)
