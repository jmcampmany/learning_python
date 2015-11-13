#!/usr/bin/env python
#-*- coding: utf-8 -*-

li = []
num = int(raw_input("Introduce números para saber si son pares o impares. Para parar introduce 0: "))

if num == 0:
	print "Acabas de empezar y ya te has aburrido. Adiós."
else:
	while num != 0:
		li.append(num)
		num = int(raw_input("Introduce números para saber si son pares o impares. Para parar introduce 0: "))
	for i in li:
		resto = i%2
		if resto == 0:
			print "El número " + str(i) + " es par."
		else:
			print "El número " + str(i) + " es impar."
