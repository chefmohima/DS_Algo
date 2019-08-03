def selection_sort(A):
    n = len(A)
    for i in range(n-1,-1,-1):
        max_index = i       # swap if found item bigger than this
        # find maximum in n-1 elements
        for j in range(i):
            if A[max_index] < A[j]:
                max_index = j
        # swap max element with last element
        A[max_index],A[i] = A[i],A[max_index]
            
        
        

# Test code    
l=[1,2,3,4,6,5]
selection_sort(l)