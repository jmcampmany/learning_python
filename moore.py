#!/usr/bin/env python
# -*- coding: utf-8 -*-

li = ((1, 0, 0, 1, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 1), (1, 0, 0, 0, 0), (0, 0, 1, 0, 0))
x = int(raw_input("Introduce el número de columna: "))
y = int(raw_input("Introduce el número de fila: "))
ficha = 0>
vecindario = li[x-1[y-1], [y], [y+1]] [x[y-1], [y+1] [x+1[y-1], [y], [y+1]]

for i in vecindario:
    if i == 1:
        ficha += 1
print int(ficha)
