f = open("D:\study\Sem 2\Python\lab\03-04-2025\Prince058_CSV.csv","a+") #\\ nakie to \ single aape
rlno = input("Enter Roll NO.[Enter to end,]")
while rlno:
    # to take full name see below
    # nm = input("Enter name")
    # cp,maths,chem = input("Enter Marks of CP, Maths and Che,istry").split()
    nm,cp,maths,chem = input("Enter Name, Marks of CP, Maths and Che,istry").split()
    f.write(rlno+','+nm+','+cp+','+maths+','+chem+'\n')
    rlno = input("Enter Roll NO.[Enter to end,]")
f.close()
