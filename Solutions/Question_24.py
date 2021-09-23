'''python has many built in functions, and if you do not know how to use it, you can read
document online or find some bookd.But python has a build in document function for
every built in function'''

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(num):
    '''Return the square value of the input number 

    The input number must be integer
    '''
    return num **2
print(square(2))
print(square.__doc__)
