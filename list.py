#! /usr/local/bin/python3

#define a list
classmates = ['jiangcw', 'gyx', 'ypf', 'lj']

print('length of list classmates: ', len(classmates))

print('classmates[0]', classmates[0])

print('classmates[-1]', classmates[-1])

classmates.append('Gdam')

print(classmates)

classmates.pop()

classmates.pop(2)

classmates[1] = 'delete gyx'

print('classmates: ', classmates)
