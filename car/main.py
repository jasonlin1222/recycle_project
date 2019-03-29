import ev3dev.ev3 as ev3 

rightm = ev3.LargeMotor('outC')
leftm = ev3.LargeMotor('outB')
col = ev3.ColorSensor('in3')
col.mode = 'COL-COLOR'
pos = 0

while True:
	try:
		leftm.run_to_rel_pos(position_sp=pos,speed_sp=20, stop_action = "hold")
		rightm.run_to_rel_pos(position_sp=pos, speed_sp=20, stop_action = "hold")
		if col.value() is 1:
			pos = 30
		else:
			pos = -30	
	except KeyboardInterrupt:
		leftm.stop()
		rightm.stop()
		exit(0)
		
