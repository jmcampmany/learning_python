#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Básicos. Ejercicio 5
li = []
num = int(raw_input("Introduce números para mostrarlos en orden inverso. Para parar introduce 0: "))

if num == 0:
	print "Acabas de empezar y ya te has aburrido. Adiós."
else:
	while num != 0:
		li.append(num)
		num = int(raw_input("Introduce números para mostrarlos en orden inverso. Para parar introduce 0: "))
	for i in reversed(li):
		print i
print "Estos son tus números invertidos. Adiós."