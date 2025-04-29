f = open("D:\\study\\Sem 2\\Python\\lab\\03-04-2025\\Prince058_CSV.csv",'r')
nisarg = f.readline()
i=1
rollno = []
nam = []
c = []
che = []
while(i<4):
    cont = f.readline()
    rolno,na,cp,mat,chem = cont.split(',')
    rollno.append(rolno)
    nam.append(na)
    c.append(cp)
    che.append(chem)
    i+=1

dic = {'Roll No.' : str(rollno), 'Name': str(nam), 'CP' : str(c), 'Chemistry' : str(che)}
print(dic)
f.close()
