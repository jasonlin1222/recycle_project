import ev3dev.ev3 as ev3 

rightm = ev3.LargeMotor('outC')
leftm = ev3.LargeMotor('outB')
col = ev3.ColorSensor('in3')
col.mode = 'COL-REFLECT'
trigger = ev3.TouchSensor('in2')
kp = 2
ki = 0
kd = 0
offset = 31
tp = -100
track = True
inter = 0
lasterr = 0
while True:
	try:
		while trigger.value():
			error = col.value() - offset
			inter = inter + error
			der = error - lasterr
			turn = kp * error + ki*inter
			powerC = tp - turn
			powerB = tp + turn
			lasterr = error
			rightm.run_forever(speed_sp = powerB)
			leftm.run_forever(speed_sp = powerC)
		rightm.stop()
		leftm.stop()
	except KeyboardInterrupt:
		leftm.stop()
		rightm.stop()
		exit(0)
		
