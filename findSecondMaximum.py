# Implement a function findSecondMaximum(lst) which returns the second largest element in the list.
# Input : [9,2,3,6] Output: 6

import pytest
class Solution:
    def findSecondMaximum(self, lst):
        if len(lst) < 2:
            return None
        if lst[0] > lst[1]:
            maxn, secmaxn = 0, 1
        else:
            maxn, secmaxn = 1, 0
  
        for i in range(2,len(lst)):
            if lst[i] > lst[maxn]:
                secmaxn = maxn
                maxn = i
            elif lst[i] > secmaxn:
                secmaxn = i
        if secmaxn:
            return lst[secmaxn]
        
        
        
class TestSolution:
    def test_findSecondMax_positiveints(self):
        s = Solution()
        assert s.findSecondMaximum([9,2,3,6]) == 6
    def test_findSecondMax_negativeints(self):
        s = Solution()
        assert s.findSecondMaximum([9,2,3,-6]) == 3
        
    def test_findSecondMax_oneelementlist(self):
        s = Solution()
        assert s.findSecondMaximum([10]) == None
