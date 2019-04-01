import ev3dev.ev3 as ev3 

rightm = ev3.LargeMotor('outC')
leftm = ev3.LargeMotor('outB')
col = ev3.ColorSensor('in3')
col.mode = 'COL-REFLECT'
kp = 10
offset = 45
tp = 5

while True:
    try:
        while True:
            error = col.value() - offset
            turn = kp * error
            powerB = tp - turn
            powerC = tp + turn
            rightm.run_forever(speed_sp = powerC)
            leftm.run_forever(speed_sp = powerB)
    except KeyboardInterrupt:
        leftm.stop()
        rightm.stop()
        exit(0)
		
