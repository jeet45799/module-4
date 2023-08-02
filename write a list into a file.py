names = []
with open(r'reading.txt', 'r') as fp:
    for line in fp:
       x = line[:-1]
       names.append(x)
print(names)
