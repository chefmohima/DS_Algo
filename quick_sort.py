import random
def quicksort(A,start,end):
    # pick random pivot index
    if start < 0 or end >= len(A) or start>=end:
        return
    pivot_index = random.randint(start,end)
    (p1,p2) = dnf(A,start,end,pivot_index)
    quicksort(A,start,p1)
    quicksort(A,p2,end)
    
def dnf(A,start,end,pivot_index):
    pivot = A[pivot_index]
    low = start-1
    mid = start-1
    high = end+1
    while mid+1 < high:
        if A[mid+1] > pivot:
            A[mid+1],A[high-1] = A[high-1],A[mid+1]
            high -= 1
        elif A[mid+1] < pivot:
            A[mid+1],A[low+1] = A[low+1],A[mid+1]
            low += 1
            mid += 1
        else:
            mid += 1
            
    return (low,high)
    
l = [10,2,3,9,6,5]
quicksort(l,0,len(l)-1)
        
    
    