#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Use two for loops, one of them nested, to print the following 5x10 rectangle:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

for i in range(10):
	for j in range(5):
		print "*",
	print