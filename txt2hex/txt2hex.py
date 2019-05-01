#!/bin/python

#hex(ord('a'))

hexa = ''
txt = input('Texto -> ')
print()

for i in txt:
	hexa += hex(ord(i)) + ' '
print(hexa)


# with open("txt2hex.txt", 'w') as file:
# 	print(hexa, file=file)