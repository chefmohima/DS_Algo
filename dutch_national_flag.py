# Program to implement Dutch National FLag problem
# You are given an array of integers and an index X.
# Rearrange the array in thefollowing order:
# [all elements less than a[X], elements equal to a[X], elements greater than a[X]],
# Similar to the Dutch National Flag (DNF).
# For example,a = [3,5,2,6,8,4,4,6,4,4,3] and i = 5
# result = [3,2,3,4,4,4,4,5,6,8,6].

def dutch_national_flag(li, pivot_index):
    pivot_value = li[pivot_index]
    low = -1
    mid = -1
    high = len(li)
    
    while high > mid+1:
        # place l[mid+1] in the right place at every iteration
        if li[mid+1] < pivot_value:
            # swap and increment low and mid
            li[mid+1], li[low+1] = li[low+1], li[mid+1]
            low += 1
            mid += 1
        elif li[mid+1] == pivot_value:
            mid = mid+1
        elif li[mid+1] > pivot_value:
            # swap and decrement high
            li[mid+1], li[high-1] = li[high-1], li[mid+1]
            high -= 1
    return li
            
input = [3,5,2,6,8,4,4,6,4,4,3]
dutch_national_flag(input,5)