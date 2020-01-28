import pytest

class Solution:
    def productExceptSelf(self, nums):
        products = []
        lefts =  [1] * (len(nums))
        rights = [1] * (len(nums))
        leftp = 1
        for i in range(len(nums)):
            lefts[i] = leftp
            leftp *= nums[i]
        
        rightp = 1
        for i in range(len(nums)-1, -1, -1):
            rights[i] = rightp
            rightp *= nums[i]
        
        for idx in range(len(nums)):
            products.append(lefts[idx] * rights[idx])
        return products
        
class TestSolution:
    def test_method_01(self):
        s = Solution()
        assert s.productExceptSelf([1,2,3,4]) == [24, 12, 8, 6]
        
        
        