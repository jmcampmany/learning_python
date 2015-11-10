#!/usr/bin/env python
# -*- coding: utf-8 -*-

grid = ((1, 0, 0, 1, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0), (0, 0, 1, 0, 0))
row = int(raw_input("Introduce el número de fila: "))
col = int(raw_input("Introduce el número de columna: "))

def count_neighbours(grid, row, col):
	count = 0
	for i in ((row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col-1)):
		if i == 1:
			count += 1
	print count
	return count
count_neighbours(grid, row, col)
