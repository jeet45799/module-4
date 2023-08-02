f=open("file function theory.txt",'a')
data=["New Delhi, national capital of India\n","It is situated in the north-central part of the country\n"," on the west bank of the Yamuna River"]
f.writelines(data)
print("Is File Readable:  ",f.readable())
print("Is File Writable:  ",f.writable())
print("Lines append to the filename file2.txt successfully")
f.close()


file1 = open("file function theory.txt")
print(file1.read())
