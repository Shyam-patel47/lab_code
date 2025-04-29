# Given a text file, write a program to create another text file deleting the words 
# ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.
f1 = open("program input.txt", "r")
f2 = open("8 program output.txt", "w")
for i in f1:
    b = i
    b = b.replace(" a ", "   ")
    b = b.replace(" the ", "   ")
    b = b.replace(" an ", "   ")
    f2.write(b)
f1.close()
f2.close()
