"""Define a function which can print a dictionary
where the keys are numbers between
1 and 3 (both included) and the values are square of keys."""


def printDict():
    
    d = dict()
    d[1] = 1
    d[2] = 2**2
    d[3] = 3**2
    print(d)
printDict()

"""def printDict(n):
    d = dict()
    for i in range(n+1):
        d[i] = i**2
    print(d)
print(printDict(3))    """
