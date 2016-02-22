def checkio(number):
	number = str(number)
	numbers = []
	for i in number:
		i = int(i)
		numbers.append(i)
    product = 1
    for i in numbers:
    	if i != 0:
			product *= i
    return product
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
