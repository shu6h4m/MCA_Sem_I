# Multiplication of two matrices using nested loops 
# By Using 3x3 matrix
n1=int(input("Enter rows of first matrix "))
m1=int(input("Enter columns of first matrix "))
print("Enter the matrix")
M1=[]
for i in range (n1):
    r=list(map(int,input().split()))
    M1.append(r)
n2=int(input("Enter rows of second matrix "))
m2=int(input("Enter columns of second matrix "))
print("Enter the matrix")
M2=[]
for i in range (n2):
    r=list(map(int,input().split()))
    M2.append(r)
    
if m1 !=n2:
    print("Product of matrices cannot be calculated ")
else:
    result = []
    for i in range(n1):
        r=[]
        for j in range(m2):
            temp=0
            for k in range(n2):
                temp += M1[i][k] * M2[k][j]
            r.append(temp)
        result.append(r)
    for r in result: 
        print(r)
            

