import math
def checkio(a, b, c):
	if a + b <= c:
		return [0, 0, 0]
	angle_a = round(math.acos((b**2 + c**2 - a**2) / (2*b*c)) / math.pi * 180)
	angle_b = round(math.acos((a**2 + c**2 - b**2) / (2*a*c)) / math.pi * 180)
	angle_c = 180 - angle_a - angle_b
	angles = [angle_a, angle_b, angle_c]
	angles.sort()
	return angles
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
