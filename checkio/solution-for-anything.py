def checkio(anything):
    """
        try to return anything else :)
    """
    return None
    
if __name__ == '__main__':
    import re, math
    
    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'
    
    print('NO WAY :(')