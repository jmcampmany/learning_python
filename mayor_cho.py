#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Desarrollar un programa en Python que solicite una lista de numeros de tamaño indeterminado por teclado y muestre por pantalla el mayor.

num = int(raw_input("Introduce números para saber el mayor de ellos. Para salir introduce un negativo: "))
mayor = num

if num < 0: #Si el número introducido es negativo sale del programa despidiéndose.
	print "Acabas de empezar y ya te has aburrido. Adiós."
else:#Si no lo es recoge números y almacena el que vaya siendo mayor en "mayor" hasta que se introduzca un negativo.
	while num >= 0:
		if num > mayor:
			mayor = num
		num = int(raw_input("Introduce números para saber el mayor de ellos. Para salir introduce un negativo: "))
	print "El mayor número es: " + str(mayor) + ". Adiós."

