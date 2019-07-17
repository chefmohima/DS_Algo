# brute-force solution
def rotate_by_one(A):
    prev = A[-1]
    # n = len(A)
    for i in range(len(A)):
        temp = A[i]
        A[i] = prev
        prev = temp

    
def rotate_array(A,k):
    for i in range(k):
        rotate_by_one(A)
    return A
    
rotate_array([1,2,3,4,5],2)

# Optimized solution with trick
def rotate_array_optimized(A,k):
    # first reverse entire array
    A.reverse()
    
    # now reverse strategically to get the result
    return A[:k][::-1] + A[k:][::-1]
    
rotate_array_optimized([1,2,3,4,5],2)