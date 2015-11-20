def checkio(array):
	out = 0
	for i in array:
		index = array.index(i)
		if index%2 == 0:
			out += i
		if index ==  len(array)-1:
			out *= i
	return out

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
