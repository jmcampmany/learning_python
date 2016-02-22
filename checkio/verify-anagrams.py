def verify_anagrams(first_word, second_word):
	first_chars = []
	second_chars = []
	first_word = first_word.replace(" ", "")
	second_word = second_word.replace(" ", "")
	for i in first_word.lower():
		first_chars.append(i)
	for i in second_word.lower():
		second_chars.append(i)
	first_chars.sort()
	second_chars.sort()
	if first_chars == second_chars:
		return True
	else:
		return False
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002
