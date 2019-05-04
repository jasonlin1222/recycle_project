import ev3dev.ev3 as ev3 

rightm = ev3.LargeMotor('outC')
leftm = ev3.LargeMotor('outB')
col = ev3.ColorSensor('in3')
col.mode = 'COL-REFLECT'
trigger = ev3.TouchSensor('in2')
kp = 1.5
ki = 0.15
kd = 15
offset = 30
tp = -150
track = True
inter = 0
lasterr = 0
while True:
	try:
		while trigger.value():
			error = col.value() - offset
			inter = inter + error
			der = error - lasterr
			turn = kp * error + ki*inter + kd*der
			powerC = tp - turn
			powerB = tp + turn
			lasterr = error
			rightm.run_forever(speed_sp = powerB)
			leftm.run_forever(speed_sp = powerC)
			print(turn)
		rightm.stop()
		leftm.stop()
	except KeyboardInterrupt:
		leftm.stop()
		rightm.stop()
		exit(0)
		
