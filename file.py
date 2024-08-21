#f = open('file1.txt','r')
#content = f.read(17)
#print(content)
#content = f.read(20)
#print(content)
#print(f.read(15))
#f.close

try:
    f = open('file1.txt','r')
    content = f.read()
    print(content)
finally:
    f.close()

with open('file1.txt','r') as f:
    content = f.read()
    print(content)