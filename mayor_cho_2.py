#!/usr/bin/env python
#-*- coding: utf-8 -*-
num = int(raw_input("Introduce números para saber el mayor de ellos. Para salir introduce un negativo: "))
lista = []

def calcula_mayor(lista):
	num = int(raw_input("Introduce números para saber el mayor de ellos. Para salir introduce un negativo: "))
	lista.append(num)
	lista.sort()
	mayor = str(lista[-1])
	return mayor

if num < 0: #Si el número introducido es negativo sale del programa despidiéndose.
	print "Acabas de empezar y ya te has aburrido. Adiós."
else:#Si no lo es recoge números y almacena el que vaya siendo mayor en "mayor" hasta que se introduzca un negativo.
	while num >= 0:
		mayor = calcula_mayor(lista)
	print "El mayor número es: " + mayor + ". Adiós."

