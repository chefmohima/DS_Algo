# Program to Move all zeroes to the end of the given integer array.
# For example, if A = [2,3,0,3,0,1,0], Output = [2,3,3,1,0,0,0].

def push_zeros(l):
    # set 2 pointers h and l
    high = 0
    low = len(l)-1
    
    while high < low:
        if l[high] != 0:
            high += 1
        else:
            # swap with element at end pointer
            l[high], l[low] = l[low],l[high]
            low -= 1
            
    return l
    
l1 = [1,2,3,0,1,2,0]
push_zeros(l1)