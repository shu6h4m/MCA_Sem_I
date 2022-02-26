

'''
Program to calculate hadamard product
Enter rows of matrix 2
Enter columns of matrix 2
Enter matrix 1
1 2
0 2
Enter matrix 2
4 5
7 8
Result
[4, 10]
[0, 16]
'''
n=int(input("Enter rows of matrix "))
m=int(input("Enter columns of matrix "))
print("Enter matrix 1")
M1=[]
for i in range (n):
    r=list(map(int,input().split()))
    M1.append(r)
print("Enter matrix 2")
M2=[]
for i in range (n):
    r=list(map(int,input().split()))
    M2.append(r)
result = []
for i in range(n):
    r=[]
    for j in range(n):
        temp=0
        temp=M1[i][j]*M2[i][j]
        r.append(temp)
    result.append(r)
print("Result")
for r in result: 
    print(r)
            

