def checkio(game_result):
    zipped = zip(game_result)
    for i in game_result:
        if "O" not in i and "." not in i:
            return "X"
        elif "X" not in i and "." not in i:
            return "O"
    for i in zipped:
        if "O" not in i and "." not in i:
            return "X"
        elif "X" not in i and "." not in i:
            return "O"
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

