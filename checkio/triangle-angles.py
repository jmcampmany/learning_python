import math

def checkio(a, b, c):
    angulo_a = math.acos((b**2+c**2-a**2)/2*b*c)
    angulo_b = math.acos((a**2+c**2-a**2)/2*a*c)
    angulo_c = 180 - angulo_a - angulo_c
    return [angulo_a, angulo_b, angulo_c]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
