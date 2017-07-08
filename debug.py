# /usr/local/bin/python3

# -*-coding:utf-8-*-

import logging
logging.basicConfig(level =  logging.INFO)

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	logging.info('info...')
	logging.warn('warn...')
	return 10 / n

if __name__ == '__main__':
	foo('1')

