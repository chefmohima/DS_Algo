# Find an item in a SORTED list, if it exists return its index, else return -1

def binary_search(l,item):
    # Initialize search space
    start, end =  0, len(l)-1 
    
    # Continue to search till there is anything to search
    while start <= end:
        mid = (start+end)//2
        if l[mid] == item:
            # found item
            return mid
        elif l[mid] > item:
            # look left for smaller elements
            end = mid-1
        elif l[mid] < item:
            # look right for higher elements
            start = mid+1
            
    return -1
    
l = [2,4,5,6,8,10,23]

binary_search(l,4)
