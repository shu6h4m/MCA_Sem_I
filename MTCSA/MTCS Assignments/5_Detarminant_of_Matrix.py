
#Program to calculate determinant of matrix

def getcofactor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]
def determinantOfMatrix(mat):
    if(len(mat) == 2):
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
    Sum = 0
    for current_column in range(len(mat)):
        sign = (-1) ** (current_column)
        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
        Sum += (sign * mat[0][current_column] * sub_det)
    return Sum
if __name__ == '__main__':
    mat = []
    n=int(input("Enter size of matrix "))
    for i in range (n):
        r=list(map(int,input().split()))
        mat.append(r)        
    print('Determinant of the matrix is :', determinantOfMatrix(mat))
