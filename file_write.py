with open ('file1.txt','w') as f:
    f.write('I love coding in python\n')
    f.write('I will master Python\n')
with open('file1.txt','a') as f:
    f.write('It will not take too long')
f = open('file1.txt','r')
print(f.read())

with open('File Handling in Python/xx/exam.txt','r') as f1:
    print(f1.read())
