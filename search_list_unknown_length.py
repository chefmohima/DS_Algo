def search_list_unknown_length(l, upper_bound, item):
    #start = 0
    # no end pointer as we do not know length of list
    end = 1
    while end < upper_bound:
        start = end
        end = end*2
    start = 0
    # do a binary search between start and end
    while start<= end:
        mid = (start+end)//2
        if l[mid] == item:
            return mid
        elif l[mid] < item:
            start = mid+1
        elif l[mid] > item:
            end = mid-1
    return -1
    

search_list_unknown_length([1,2,4,9,12,16],4,2)
    
    

        
    