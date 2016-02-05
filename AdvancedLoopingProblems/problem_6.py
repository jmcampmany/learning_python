#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""	
Write code that will print the following:

Use two nested loops. Print the first line with a loop, and not with:
print("0 1 2 3 4 5 6 7 8 9")
"""

for i in range(10):
	count = 0
	for j in range(10):
		print count,
		count += 1
	print