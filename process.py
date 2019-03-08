import ev3dev.ev3 as ev3
import time
import pickle as pk
import ui as i
import os



def startsys():
    os.system("python3 system.py")
def endsys():
    with open("userdata.txt", "w+") as file:
       	for i in range(len(i.arr))
        	pk.dump(, file)
    print("exit system in 5 second.....")
    time.sleep(5)
    exit(0)
