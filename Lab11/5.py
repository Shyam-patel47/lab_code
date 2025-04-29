# Write a program to copy contents of one file to another. While doing so,
# replace all lowercase characters into uppercase characters.

f1 = open("D:\\study\\Sem 2\\Python\\lab\\03-04-2025\\program input.txt", "r")
f2 = open("D:\\study\\Sem 2\\Python\\lab\\03-04-2025\\program output.txt", "w")
f2.write(f1.read().upper())
f1.close()
f2.close()  