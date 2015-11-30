def days_diff(date1, date2):
	days = (date1[0]-date2[0])*365 + (date1[1]-date2[1])*30 + (date1[2]-date2[2])
    return abs(days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
