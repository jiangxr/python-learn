#! /usr/local/bin/python3

def count():
	def f(i):
		def g():
			return i * i
		return g;
	tt = []
	for i in range(1, 4):
		tt.append(f(i))
	return tt

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
