#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Básicos. Ejercicio 3

li = []
num = int(raw_input("Introduce números para sumarlos. Para parar introduce 0: "))

if num == 0:
	print "Acabas de empezar y ya te has aburrido. Adiós."
else:
	while num != 0:
		li.append(num)
		num = int(raw_input("Introduce números para sumarlos. Para parar introduce 0: "))
	total = 0
	for i in li:
		total += i
print "El resultado a la suma de todos tus números es " + str(total) + ". Adiós."

