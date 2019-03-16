import ev3dev.ev3 as ev3
import time
import ui as i

colors = ('unknown black blue green yellow red white brown'.split())
while True
	if i.ts.is_pressed:
		trash = True
		print("processing......")
		print("insert your card and hold still.....")
		time.sleep(5)
		card = colors[i.coldoor.value()]
		while card is "unknown":
			print("card is not detected")
			card = colors[i.coldoor.value()]
		i.doorm.run_to_rel_pos(speed_sp = 100, position_sp = 90) #opmitize result
		while colors[i.colin.value()] is "unknown":
			print("waiting for trash...")
		while colors[i.colin.value()] is not "red" or "blue":
			print("error")
		if colors[i.colin.value()] is "red":
			i.user[card].trash += 1
		elif colors[i.colin.value()] is "blue":
			i.user[card].recycle += 1
