'''Write a program that accepts a sentence and calculate the number of letters
and digits. Suppose the following input is supplied to the program: hello
world! 123 Then, the output should be: LETTERS 10 DIGITS 3'''

#take the imput from the user
s = input()
#set the dictionary
d = {"DIGITS": 0, "LETTERS": 0}

#loop through s to count the numbers and alphabet

for count in s:
    if count.isdigit():
        d["DIGITS"] += 1
    elif count.isalpha():
        d["LETTERS"] += 1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])
