#! /usr/local/bin/python3

# -*- coding:utf-8 -*-

class Student(object):
	def __init__(self, name, score, age):
		self.name = name
		self.score = score
		self.__age = age
	def print_score(self):
		print('%s %s' %(self.name, self.score))

	def hello(self):
		print('hello, world!!')
