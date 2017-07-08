class A(object):
	
	def __init__(self, value1, value2, value3, value4, value5):
		self.value1 = value1
		self.___value2 = value2
		self.__value3__ = value3
		self._value4 = value4
		self.__value5_ = value5

	def __method1(self):
		print('method1')

	def _method2(self):
		print('method2')

	def __method3__(self):
		print('method3')

	def __method4_(self):
		print('method4')
		
