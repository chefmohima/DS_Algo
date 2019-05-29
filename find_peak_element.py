def find_peak(l):
    # find  first peak
    # if index of peak = i where i > 0 or i+1 <= len(l)-1
    # then l[i-1] < l[i] > l[i+1]
    
    if len(l) == 1 :
        return 0
    
    start = 0
    end = len(l) - 1
    
    while start <= end :
        mid = (start+end)//2
        if (mid == 0 and l[mid] > l[mid+1]) or \
        (mid == len(l)-1 and l[mid-1] < l[mid]) or \
        (l[mid-1] < l[mid]) and (l[mid+1] < l[mid]):
            return mid
        elif l[mid+1] > l[mid] and l[mid-1] > l[mid]:
            # peak can be on any side, find higher value
            if l[mid+1] > l[mid-1]:
                start = mid+1
            else:
                end = mid-1
        elif l[mid-1] > l[mid]:
            # search left
            end = mid-1
        elif l[mid+1] > l[mid]:
            # search left
            start = mid+1
    
    
print(find_peak([5,6,1,2,3]))
print(find_peak([1,2,3,4,5]))
print(find_peak([5,4,3,2,1]))
print(find_peak([1,5,2,3,1,4]))
        
    