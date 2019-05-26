# Given a sorted array that can contain duplicates, find the first occurrence of thetarget element. 
# For example:A=[1,3,4,6,6,6,7] and Target=6,returnindex3.
def binary_search_first_index(l,item):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start+end)//2
        if l[mid] == item:
            # first index can only be on the left, otherwise mid is the first index
            i = mid-1
            while i >= start:
                if l[i] != item:
                    break
                i = i-1
            return i + 1
        
        elif l[mid] > item:
            end = mid-1
        elif l[mid] < item:
            start = mid+1
            
    return -1
    
l = [2,4,4,4,4,5,6,8,10,10,10,10,10,10,23]

binary_search_first_index(l,10)

    
        
        
        
