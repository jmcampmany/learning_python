#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Básicos. Ejercicio 4

li = []
num = int(raw_input("Introduce números para operar con ellos. Para parar introduce 0: "))

if num == 0:
	print "Acabas de empezar y ya te has aburrido. Adiós."
else:
	while num != 0:
		li.append(num)
		num = int(raw_input("Introduce números para operar con ellos. Para parar introduce 0: "))
	op = str(raw_input("Indica si quieres sumar o restar: "))
	resultado = num
	if op == "sumar":
		for i in li:
			resultado += i
	elif op == "restar":
		for i in li:
			resultado -= i
	else:
		print "Debes de haberte equivocado introduciendo el operador, introduce \"sumar\" o \"restar\""
print "El resultado a la suma de todos tus números es " + str(resultado) + ". Adiós."