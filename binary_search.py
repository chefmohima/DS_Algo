# Find an item in a SORTEDlist, if it exists return its index, else return -1

def binary_search(l,item):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start+end)//2
        if l[mid] == item:
            return mid
        elif l[mid] > item:
            end = mid-1
        elif l[mid] < item:
            start = mid+1
            
    return -1
    
l = [2,4,5,6,8,10,23]

binary_search(l,4)