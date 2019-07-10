# All array rotations are a combination of 
# transpose, reverse rows and reverse columns

# helper
def transpose(A):
    row,col = len(A),len(A[0])
    
    # create empty matrix colxrow
    T = [[0]*row for i in range(col)]
    
    for i in range(row):
        for j in range(col):
            T[i][j] = A[j][i]
    return T

# helper
def reverse_row(A):
    row,col = len(A),len(A[0])
    for i in range(row):
        start,end = 0,col-1
        while start != end:
            A[i][start],A[i][end] = A[i][end],A[i][start]
            start += 1
            end -= 1
    return A

# helper	
def reverse_col(A):
    row,col = len(A),len(A[0])
    for j in range(col):
        start,end = 0,row-1
        while start != end:
            A[start][j],A[end][j] = A[end][j],A[start][j]
            start += 1
            end -= 1
    return A
    
def rotate_by_90(A):
    T = transpose(A)
    return reverse_row(T)
    
def rotate_by_minus90(A):
    T = transpose(A)
    return reverse_col(T)
    
def rotate_by_180(A):
    return reverse_col(reverse_row(A))
    
def rotate_by_minus180(A):
    return reverse_row(reverse_col(A))
    
    
# Test
A = [[1,2,3],
    [3,4,5],
    [6,7,8]]
    
# print(transpose(A))
# print(reverse_row(A))
# print(reverse_col(A))

print(rotate_by_90(A))
print(rotate_by_minus90(A))
print(rotate_by_180(A))
print(rotate_by_minus180(A))
    