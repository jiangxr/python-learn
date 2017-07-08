#! /usr/local/bin/python3

def add_end(L = []):
	L.append("END")
	return L

def add_end2(L = None):
	if L is None:
		L = []
	L.append("END")
	return L
