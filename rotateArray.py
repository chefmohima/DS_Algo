# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]


import pytest

class Solution:
    
    # O(N*N) solution : for understanding only
    def rotate(self, nums, k):
        # shift element by 1
        # repeat k times
        for i in range(k):
            lastNum = nums[-1]
            j = len(nums)-1
            while j > 0:
                nums[j] = nums[j-1]
                j -= 1
            nums[0] = lastNum
        return nums
        
    # O(N) solution
    def rotate_On(self, nums, k):
        # find index of rotation where it begins, k elements from the end of list
        n = len(nums)-k
        return nums[n:] + nums[:n]
    




class TestSolution:
    def test_rotate_example(self):
        s = Solution()
        assert s.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
        
    def test_rotate_kisgreaterthanlistlength(self):
        s = Solution()
        assert s.rotate([1,2,3,4,5,6,7], 8) == [7,1,2,3,4,5,6]
        
    def test_rotate_On(self):
        s = Solution()
        assert s.rotate_On([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
        
        
        
    