import math

class Point:
       def __init__(self):
             self.a = 0
             self.b = 0

def dist_between_points(x,y):
       d1 = x.a - y.a
       d2 = x.b - y.b
       dist =math.sqrt(d1**2 + d2**2)
       return dist

a = Point()
b = Point()
print(a)
print(b)
print(a !=b)

p0 = Point()
p0.a = 14
p0.b = 18

p1 = Point()
p1.a = 20
p1.b = 25
print('distance')
print(dist_between_points(p1,p0))
