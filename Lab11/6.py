# Write a program that merges lines alternatively from two files and writes the results to new file.
# If one file has less number of lines than the other,  
# the remaining lines from the larger file should be simply copied into the target file.
f1 = open('program input.txt','r')
f2 = open('program output.txt','r')
f3 = open('6 program output.txt','w')
while True:
    line1 = f1.readline()
    line2 = f2.readline()
    if (not line1) and (not line2):
        break
    if line1:
        f3.write(line1.rstrip('\n') + '\n')
    if line2:
        f3.write(line2.rstrip('\n') + '\n')
f1.close()
f2.close() 
f3.close()