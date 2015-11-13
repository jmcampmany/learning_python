#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Básicos. Ejercicio 2

entrada = int(raw_input("Introduce un número par para obtener Hola o un impar para obtener Adiós."))

if  entrada%2 == 0:
	print "Hola"
else:	
	print "Adiós"
