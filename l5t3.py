class Time:
	def __init__(self):
		self.hour = 0
		self.minute = 0
		self.second = 0
	

def print_time(time):
	print("%.2d:%.2d:%.2d" %(time.hour,time.minute,time.second))




time = Time()
time.hour = 13
time.minute = 39
time.second = 15
print_time(time)

