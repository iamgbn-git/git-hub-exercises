#Question 41
"""DEfine a function which can generate and print a tuple where the value are square of
nubmers between 1 and 20(both included)"""


def printTuple():

    li = list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))
printTuple()
