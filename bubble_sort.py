def bubble_sort(A):
    n = len(A)
    passnum = 0
    for i in range(n-1,0,-1):
        passnum += 1
        for j in range(i):
            if A[j+1] < A[j]:
                A[j+1],A[j] = A[j],A[j+1]
    print(passnum)
    return A


def bubble_sort_optimized(A):
    n = len(A)
    passnum = 0
    for i in range(n-1,0,-1):
        passnum += 1
        for j in range(i):
            swapnum=0
            if A[j+1] < A[j]:
                swapnum += 1
                A[j+1],A[j] = A[j],A[j+1]
        if swapnum == 0:
            break
    print(passnum)
    return A
    
        
        

# Test code    
l=[1,2,3,4,6,5]
bubble_sort(l)
l=[1,2,3,4,6,5]
bubble_sort_optimized(l)