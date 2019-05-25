# Given an array of integers that can be both +ve and -ve, 
# find the contiguous subarraywith the largest sum.e.g, [1,2,-1,2,-3,2,-5]  -> the first 4 elements have the largest sum

# The main assumption is the max sum at any index i of array A must include the cumulative sum at index i-1, say B[i-1]
# only if it is non-negative, ie: A[i] = max(A[i], A[i]+B[i-1])	
def maxSubArray(nums):
     
 
        nums[-1] = 0
        for i in range(len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
        return max(nums)
        
l = [1,2,-1,2,-3,2,-5]
maxSubArray(l)