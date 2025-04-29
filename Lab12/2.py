#2.	Write a program that implements a Matrix class and performs addition, 
# multiplication and transpose operations on 3x3 matrices.

class matrix:
    def addition(self,a,b):
        for i in range(3):
            for j in range(3):
                print(a[i][j]+b[i][j], end = ' ')
            print()
    
    def multiplication(self,a,b):
        for i in range(3):
            for j in range(3):
                c = 0
                for k in range(3):
                    c += int(a[i][k]*b[k][j])
                print(c, end = ' ')
            print()
    
    def transpose(self,a):
        for i in range(3):
            for j in range(3):
                print(a[j][i], end = ' ')
            print()    
print("input the first matrix:")       
a = [[int(input(f"input{j,i} element")) for i in range(3)] for j in range(3)]
print("input the second matrix:")
b = [[int(input(f"input{j,i} element")) for i in range(3)] for j in range(3)]
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             a[i][j] = 1
#             b[i][j] = 1
#         else:
#             a[i][j] = 0
#             b[i][j] = 0
m = matrix()
print("the addition of two matrices is:")
m.addition(a,b)
print('the multiplication of two matrices is:')
m.multiplication(a,b)
print('the transpose of the first matrix is:')
m.transpose(a)
print('the transpose of the second matrix is:')
m.transpose(b)