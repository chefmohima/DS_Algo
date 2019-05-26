# You are given a sorted array A and a target T. 
# If the target is found, return the index. If not, return the index where it would be placed if inserted in order. For example,
# A = [1,2,4,5,6,8] and T = 3, return index 2
# A = [1,2,4,5,6,8] and T = 0, return index 0


def binary_search_index_to_insert_item(l,item):
    start = 0
    end = len(l)-1
    
    start_diff = float('inf')
    while start <= end:
        mid = (start+end)//2
        diff = abs(item-l[mid])
        if diff == 0:
            return mid
        if diff < start_diff:
            start_diff = diff
            closest = mid
        #if l[mid] == item:
            #return mid
        elif l[mid] > item:
            end = mid-1
        elif l[mid] < item:
            start = mid+1
    
    if item > l[closest]:
        return closest+1
    else:
        return closest-1
    
l = [2,4,4,4,4,5,6,8,10,10,10,10,10,10,21,23]

binary_search_index_to_insert_item(l,9)