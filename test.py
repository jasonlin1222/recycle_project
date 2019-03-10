
class usercolor:
	def __init__(self):
		self.password = ''
		self.money = 0
		self.trash = 0
		self.recycle = 0
		self.username = ''

coloru = input()

exec(coloru + '= usercolor()')
exec(coloru + ".username = str(input('enter your name:'))")
exec(coloru + ".password = str(input('enter your password:'))")

print(coloru)