f = open('file.txt', 'w')
f.write("Hello World!")
f.close()

f = open('file.txt', 'r')
print(f.read())
f.close()

f = open('file.txt', 'a')
f.write("\nHello again!")
f.close()

f = open('file.txt', 'r')
print(f.read())
f.close()

f = open('file.txt', 'w')
f.write("Where is my previous text?")
f.close()

f = open('file.txt', 'r')
print(f.read())
f.close()


with open('file.txt', 'w') as f:
    f.write("I don't need to close the file anymore!")
