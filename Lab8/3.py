def create_array(a,b,c,n):
    arr = [[[0 for _ in range(c)] for _ in range(b)] for _ in range(a)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                    arr.append([n])
        for i in range(a):
            for j in range(b):
                for k in range(c):
                    print(arr[i][j][k], end=" ")
                print()
            print()

n = int(input("enter number you want in array: "))
create_array(3,4,5,n)