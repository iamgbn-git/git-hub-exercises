fh = open("test.txt", 'r')
result = [i for i in fh if "line3" in i]
print(result)
