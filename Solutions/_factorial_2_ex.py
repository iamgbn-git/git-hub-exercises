

'''write a program which can compute the factorial of a given numbers.
The results  should be printed in a comma-separated sequence on a single line.
Suppose the following is supplied to the program:8. Then the output should
be 40320'''


def factorial(x):
    if x == 0:
        return 1
    else:
        fact = 1
        for i in range(x):
            fact = fact * (x-i)
    return fact
x = int(input("Enter Number: "))
print(factorial(x))
