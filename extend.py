class A1(object):
	def run(self):
		print('run A1')

class A2(object):
	def run(self):
		print('run A2')

class A3(A1, A2):
	def run(self):
		print('run A3')

class B(object):
	def run(self):
		print('run B')

class C(object):
	def invoke(self, a1):
		a1.run()

c = C()
a1 = A1()
a2 = A2()
A1 a3 = A3()
b = B()
c.invoke(a1)
c.invoke(a2)
c.invoke(a3)
c.invoke(b)
