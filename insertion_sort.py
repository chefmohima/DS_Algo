def insertion_sort(A):
    n = len(A)
    for i in range(1,n):        # 0th element is sorted
        key = A[i]              # place this in correct position
        j = i-1
        while j >=0 and A[j] > key:
            # shift elements right to make place for key
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A
            
            
        
        

# Test code    
l=[1,2,3,4,6,5]
insertion_sort(l)