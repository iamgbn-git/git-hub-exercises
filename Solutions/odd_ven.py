"""Define a function that can accept an integer number as input and
print the "It is an even number"
if the number is even, otherwise print "It is an odd number"."""

def oddEven(num):
    if num % 2 == 0:
        return "It is an even number"
    else:
        return "The number is odd."



num = int(input("Enter any number: "))
print(oddEven(num))   
