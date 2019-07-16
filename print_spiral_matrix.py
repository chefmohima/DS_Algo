def matrix_traverse_spiral(A):
    m,n = len(A),len(A[0])
    T,B,L,R = 0,2,0,2
    dir = 'right'
    
    while T <= B and L <= R:
        if dir == 'right':
            for i in range(L,R+1):
                print(A[T][i])
            T += 1
            dir = 'down'
        if dir == 'down':
            for i in range(T,B+1):
                print(A[i][R])
            R -= 1
            dir = 'left'
        if dir == 'left':
            for i in range(R,L-1,-1):
                print(A[B][i])
            B -= 1
            dir = 'up'
        if dir == 'up':
            for i in range(B,T-1,-1):
                print(A[i][L])
            L += 1
            dir = 'right'
            
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
     
matrix_traverse_spiral(A)
        