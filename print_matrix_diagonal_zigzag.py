def print_diagonal_matrix(A):
    row,col = len(A),len(A[0])
    diags = [[] for i in range(row+col-1)]
    for i in range(row):
        for j in range(col):
            diags[i+j].append(A[i][j])
    
    # reverse direction for odd diagonals
    for i in range(len(diags)):
        if i%2 != 0:
            diags[i].reverse()
            print(diags[i])
        else:
            print(diags[i])
            
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
     
print_diagonal_matrix(A)