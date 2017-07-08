#! /usr/local/bin/python3

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

while True:
	x = input('please enter value:')
	x = float(x)
	if x == 0:
		break;
	print(my_abs(x))
