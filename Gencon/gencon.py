#!/bin/python3

import sys
from random import randint
from linecache import getline

#funciones
def ayuda():
	print("USO:")
	print("gencon.py [-n NUM] [-s SEPARADOR] [-d DICCIONARIO] [-f SALIDA] [-l LETRA]")
	exit()

def palabraQueEmpiezaPor(l):
	pal = " "
	while pal[0] != l:
		pal = getline(diccionario, randint(1, n))[:-1]
	return pal


#valores predeterminados
contra = ""
diccionario = "SP_wordlist.lst"
num_pal = 4
separador = " "
salida = False
primera_letra = False

#procesar argumentos
for i in range(1, len(sys.argv)):
	if sys.argv[i] == "-h" or sys.argv[i] == "--help":
		ayuda()
	if sys.argv[i] == "-n":
		num_pal = int(sys.argv[i+1])
	if sys.argv[i] == "-s":
		separador = sys.argv[i+1]
	if sys.argv[i] == "-d":
		diccionario = sys.argv[i+1]
	if sys.argv[i] == "-f":
		salida = sys.argv[i+1]
	if sys.argv[i] == "-l":
		primera_letra = sys.argv[i+1]


#parte principal
with open(diccionario, 'r') as f:
	n = len(f.readlines())

if primera_letra:
	for i in range(1, num_pal):
		contra = contra + palabraQueEmpiezaPor(primera_letra)
		contra = contra + separador
	contra = contra + palabraQueEmpiezaPor(primera_letra)
else:
	for i in range(1, num_pal):
		contra = contra + getline(diccionario, randint(1, n))[:-1]		#[:-1] es para quitar \n
		contra = contra + separador
	contra = contra + getline(diccionario, randint(1, n))[:-1]

if salida:
	with open(salida, 'a') as f:
		f.write(contra+"\n")
else:
	print(contra)
