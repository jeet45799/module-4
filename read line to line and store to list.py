with open('reading.txt') as f:
    content = f.readlines()

li = [x.strip() for x in content]
print(li)
