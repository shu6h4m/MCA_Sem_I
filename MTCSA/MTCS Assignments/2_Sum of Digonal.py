'''
Program to calculate Sum of diagonal elements of the matrix
Enter size of matrix 3
1 4 7
2 5 8
3 6 9
Sum of diagonal elements of the matrix is : 15
'''
def diag_sum(mat):
    Sum=0
    for i in range(len(mat)):
        Sum+=mat[i][i]   
    return Sum
if __name__ == '__main__':
    mat = []
    n=int(input("Enter size of matrix "))
    for i in range (n):
        r=list(map(int,input().split()))
        mat.append(r)        
    print('Sum of diagonal elements of the matrix is :', diag_sum(mat))
