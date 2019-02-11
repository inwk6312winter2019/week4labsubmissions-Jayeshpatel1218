from l5t3 import Time

def is_after(t1,t2):
	return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


time = Time()
time.hour = 13
time.minute = 39
time.second = 15


time1 = Time()
time1.hour = 18
time1.minute = 55
time1.second = 45

print(is_after(time1,time))
