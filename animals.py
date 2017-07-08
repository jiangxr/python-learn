#! /usr/local/bin/python3
# -*-coding:utf-8 -*-

class Person(object):
	def speak(self):
		print('people can speak')

class Man(Person):
	def speak(self):
		print('man can speak')

class Women(Person):
	def speak(self):
		print('women can speak')

def run(person):
	person.speak()

a = Person()
b = Man()
c = Women()

run(a)
run(b)
run(c)
