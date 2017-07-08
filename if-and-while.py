#! /usr/local/bin/python3

age = 10

if age > 20:
	print('age is larger than 20')
elif age > 10:
	print('age is larger than 10')
else:
	print('age is not larger than 10')

sum = 0
for m in range(101):
	sum += m;
print('sum = %d' %(sum) )
