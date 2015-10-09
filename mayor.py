#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Desarrollar un programa en Python que solicite una lista de numeros de tamaño indeterminado por teclado y muestre por pantalla el mayor.

mayor = 0
aburrido = False
while not aburrido:
	num = int(raw_input("Introduce un número positivo. Introduce un negativo para terminar."))
	if num > mayor:
		mayor = num

	if num < 0:
		aburrido = True

print "El mayor es " + str(mayor)