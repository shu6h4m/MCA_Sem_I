'''
Program to calculate Outer product
Enter first vector 
1 2 3
Enter second vector 
1 2
Original Vector:
[1, 2, 3]
[1, 2]
Outer Product of the two vectors is:
[[1, 2], [2, 4], [3, 6]]
'''
print("Enter first vector ")
A=list(map(int,input().split()))
print("Enter second vector ")
B=list(map(int,input().split()))
print("Original Vector:") 
print(A) 
print(B) 
print("Outer Product of the two vectors is:")
ans=[]
for i in range(len(A)):
    r=[]
    for j in range(len(B)):
        t=0
        t+=A[i]*B[j]
        r.append(t)
    ans.append(r)
print(ans) 
