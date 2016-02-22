def checkio(first, second):
	count = 0
	commonWords = []
	first = first.split(",")
	second = second.split(",")
	for word in first:
		if word in second:
			commonWords.append(word)
    return ",".join(sorted(commonWords))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
