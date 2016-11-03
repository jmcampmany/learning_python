#!/usr/bin/env python 
#-*- coding: utf-8 -*-
#Función que reciba una lista de números y sume solamente los positivos.

def sumaPositivos (numeros):
	total = 0
	for i in numeros:
		if i >= 0:
			total += i
	return total