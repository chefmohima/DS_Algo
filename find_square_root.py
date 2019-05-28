def find_square_root(num):
    if num == 0 or num == 1:
        return num
    # do a binary search
    start = 1
    end = num
    
    while start<= end:
        mid = (start+end) // 2
        if mid*mid == num:
            return mid
        elif mid*mid > num:
            # look left
            end = mid-1
        elif mid*mid < num:
            start = mid+1
            
find_square_root(25)