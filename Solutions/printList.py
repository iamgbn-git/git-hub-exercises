#Question 37
"""Define a function which can generate a list where the values are square of
numbers between 1 and 20 (both included).
Then the function needs to print the first 5 elements in the list."""

def printList(n):
    
    li = []
    for i in range(1,n+1):
       li.append(i**2)
    return(li[::3])
        
print(printList(20))
