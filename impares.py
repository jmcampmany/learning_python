#!/usr/bin/env python 
#-*- coding: utf-8 -*-
#Función que reciba una lista y devuelva otra lista solamente con los elementos de índice impar

def devuelveImpares (numeros):
	impares = []
	impar = False
	for i in numeros:
		if impar == True:
			impares.append(i)
			impar == False
		else:
			impar == True
	return impares