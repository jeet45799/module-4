with open('file function theory.txt','r') as firstfile, open('reading.txt','a') as secondfile:
    for line in firstfile:
                secondfile.write(line)
f = open('reading.txt', 'r')
content=f.read()
print(content)
