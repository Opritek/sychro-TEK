import math
def c(x):
	y = math.cos(x)
	return y
def s(x):
	h = math.sin(x)
	return h
def t(x):
	g = math.tan(x)
	return g
def acos(x):
	z = math.acos(x)
	return z
def asin(x):
	q = math.asin(x)
	return q
def atan(x):
	p = math.atan(x)
	return p	
import time
localtime = time.asctime( time.localtime(time.time()) )
print (localtime)
print('\nHello!\n\nOptions\n\nTo solve for angle enter:\n\narcsin, arccos, or arctan the value\n\n\nTo solve for the trigonometric value of an angle enter:\n\nsin, cos, tan, of the angle\n\nNote; ensure there is no space before the values')
user = input('\nEnter your choice\n\n')
user = user.upper()
q = user[:3]
if q == 'SIN':
	t = float(user[3:])
	x = math.radians(t)
	s = s(x)
	print('\nsin',round(t,4),'=',s)
elif q == 'COS':
	u = float(user[3:])
	x = math.radians(u)
	e = c(x)
	print('\ncos',round(u,4),'=',e)
elif q == 'TAN':
	w = float(user[3:])
	x = math.radians(t)
	t = t(x)
	print('\ntan',round(w,4),'=',d)
elif user[:6] == 'ARCSIN':
	x = float(user[6:])
	k2 = asin(x)
	k2 = math.degrees(k2)
	print('\nsin-¹',round(x,4),'=',k2)
elif user[:6] == 'ARCCOS':
	x = float(user[6:])
	m = acos(x)
	m = math.degrees(m)	
	print('\ncos-¹',round(x,4),'=',m)
elif user[:6] == 'ARCTAN':
	x = float(user[6:])
	V = atan(x)
	V = math.degrees(V)	
	print('\ntan-¹',round(x,4),'=',V)		
else:
	print('U N K N O W N  I N P U T')
