def find_min_sorted_rotated_list(l):
    start = 0
    end = len(l)-1
    last = l[end]       # this is used as pivot to segregate the array
    
    # start with searching minimum value
    # in a sorted rotated list the minimum value will always be less than the last value
    # also if index of min value = i, then l[i-1] is always greater than l[i]
    # with the exception of when the minimum is the first element at index 0
    while start <= end :
        mid = (start+end)//2
        if l[mid] < last and (l[mid-1] > l[mid] or mid == 0):
            return mid
        
        # if min not found, determine if mid is at left or right section of the list
        elif l[mid] > last:
            # mid is towards the left of the list and needs to move right
            start = mid + 1
        elif l[mid] < last:
            # mid is at the right of pivot, needs to move left
            # min element should be at the leftmost index of the section right of pivot
            end = mid-1
            
    
l = [1,2,3,4,6,8]
find_min_sorted_rotated_list(l)
    
    
    

        
    