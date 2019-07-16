def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row,col = len(matrix),len(matrix[0])
        found = False
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    found = True
                    break
            if found:
                break
                
            
        for p in range(row):
            for q in range(col):
                if p == i or q == j:
                    matrix[p][q] = 0
        return matrix
        
            
A = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
     
setZeroes(A)