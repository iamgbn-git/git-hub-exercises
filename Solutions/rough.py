import math 
c = 50
h = 30
value = []
n  = input("Enter anything:  ")
items = n.split(",")
for d in items:
    value.append(str(int(math.sqrt(2*c*float(d)/h))))
print(','.join(value))

