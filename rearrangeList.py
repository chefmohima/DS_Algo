#Implement a function reArrange(lst) 
#which rearranges the elements such that all the negative elements
# appear on the left and positive elements appear at the right. 
# Input: [10,-1,20,4,5,-9,-6]
# Output: [-1,-9,-6,10,20,4,5]


import pytest

class Solution:
    
    def reArrange(self, lst):
    # Write your code here
        lastNegativeIndex = 0
        for curr in range(len(lst)):
            if lst[curr] < 0 and curr > 0:
                
                # need to move left by swapping
                # determine which index to move to
                if lst[lastNegativeIndex] < 0:
                    lastNegativeIndex += 1
                j = curr
                while (j != lastNegativeIndex):
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                    j -= 1
        return lst
    




class TestSolution:
    def test_rearrange_list1(self):
        s = Solution()
        assert s.reArrange([-1, 2, -3, -4, 5]) == [-1, -3, -4, 2, 5]
        
    def test_rearrange_list2(self):
        s = Solution()
        assert s.reArrange([300, -1, 3, 0]) == [-1, 300, 3, 0]
        
    
    def test_rearrange_list3(self):
        s = Solution()
        assert s.reArrange([0, 0, 0, -2]) == [-2, 0, 0, 0]
        
    
        
        
        
    