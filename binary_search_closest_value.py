# Given a sorted array A and a target T, find the target. If the target is not in the array, find the number closest to the target. 
# For example, if A = [2,3,5,8,9,11] and T = 7, return 8.

def binary_search_closest(l,item):
    start = 0
    end = len(l)-1
    
    start_diff = float('inf')
	
    while start <= end:
        mid = (start+end)//2
        
		diff = abs(item-l[mid])
        if diff == 0:
            return mid
        # record index of mid if diff between item and l[mid] is lowest till this iteration
		if diff < start_diff:
            start_diff = diff
            closest = mid
        #if l[mid] == item:
            #return mid
        elif l[mid] > item:
            end = mid-1
        elif l[mid] < item:
            start = mid+1
            
    return closest
    
l = [2,4,4,4,4,5,6,8,10,10,10,10,10,10,21,23]

binary_search_closest(l,20)