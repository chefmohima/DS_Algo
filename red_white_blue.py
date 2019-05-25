# Given an array with n objects colored Red, White or Blue, 
# sort them so that objects of the same color are adjacent, 
# with the colors in the order Red, White and Blue. 
# Assume the colors are given as numbers - 0 (Red), 1 (White) and 2 (Blue).
# For example, if A = [1,0,1,2,1,0,1,2], Output = [0,0,1,1,1,1,2,2].
# Solution same as dutch nationa flag


def red_white_blue(l):
    pivot = 1 # as 1 is the value for mid section
    low = -1 
    mid = -1
    high = len(l)
    while mid+1 < high:
        if l[mid+1] < 1:
            # place in low
            l[mid+1], l[low+1] = l[low+1], l[mid+1]
            low += 1
            mid += 1
        elif l[mid+1] == 1:
            # place in mid section, no swaps needed
            mid = mid+1
        elif l[mid+1] >= 1:
            # place in high section
            l[mid+1], l[high-1] = l[high-1], l[mid+1]
            high -= 1
    return l
    
red_white_blue([1,0,1,2,1,0,1,2])