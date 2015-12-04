OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
def boolean(x, y, operation):
	if operation == "conjunction":
		if x and y:
			return 1
		else:
			return 0
	if operation == "disjunction":
		if x or y:
			return 1
		else:
			return 0
	if operation == "implication":
        if x:
            return y
        else:
            return 1
	if operation == "exclusive":
		if x == y:
			return 0
		else:
			return 1
	if operation == "equivalence":
		if x == y:
			return 1
		else:
			return 0
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
