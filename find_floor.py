# Given an array of numbers sorted in an ascending order, find the floor of a given number ‘key’
# The floor of the ‘key’ will be the largest element in the given array smaller than or equal to the ‘key’.
# Write a function to return the floor of the ‘key’. If there isn’t any ceiling return -1.
# Example: Floor of key 12 in a list [1, 3, 8, 10, 15] = 10


def search_floor_of_a_number(nums, key):
    # if key < smallest num in list then floor cannot exist
    if key < nums[0]:
        return -1
    # do normal binary search
    # return key of found
    # else return end index
    # As loop runs till start <= end, if key is not found then, start index 
    # will exceed end index
    start, end = 0, len(nums)-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == key:
            return nums[mid]
        elif nums[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return nums[end]
    
print(search_floor_of_a_number([4, 6, 10], 6))
print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
print(search_floor_of_a_number([4, 6, 10], 17))
print(search_floor_of_a_number([4, 6, 10], -1))
