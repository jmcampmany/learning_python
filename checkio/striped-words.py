VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
	flag = True
	flag2 = False
	while flag == True xor flag2 == True:
		for i in text:
			if i in VOWELS:
				flag = True
			else:
				flag = False
			if i in CONSONANTS:
				flag2 = True
			else:
				flag = False


    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
