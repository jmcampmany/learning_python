def checkio(data):
    data.sort()
    if len(data)%2 != 0:
        median = (len(data)+1)/2
    else:
        median = (len(data)/2 + (len(data)+1)/2)/2
    return median