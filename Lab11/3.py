# make excel and add name and mob no and make v card 
# Accept contact details from the user and create a vcard that we can directly store in our mobile.
f1 = open('Name and Mobile No.csv', 'r')
f2 = open('vcard.vcf','w')
while True:
    line = f1.readline()
    if not line:
        break
    name, mob = line.split(',')
    f2.write('BEGIN:VCARD\n')
    f2.write('VERSION:3.0\n')
    f2.write('N:%s\n' % name)
    f2.write('TEL;TYPE=CELL:%s\n' % mob)
    f2.write('END:VCARD\n')
f1.close()
f2.close()