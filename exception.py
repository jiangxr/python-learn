#! /usr/local/bin/python3

# -*-coding:utf-8-*-

import logging

def excep():
	try:
		print("try...")
		r = 10 / 0 
		print('result:', r)
	except ZeroDivisionError as e:
		logging.exception(e)
		raise
	else:
		print('else...')
	finally:
		print('finally...')
	print('END')

excep()
		
