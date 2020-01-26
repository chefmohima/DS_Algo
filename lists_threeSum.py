# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:
            def twoSum(l, val):
                result = []
                start, end = 0, len(l)-1
                while start < end:
                    calc_sum = l[start]+l[end]
                    if calc_sum > val:
                        end -= 1
                    elif calc_sum < val:
                        start += 1
                    else:
                        newlist = []
                        newlist.append(l[start])
                        newlist.append(l[end])
                        result.append(newlist)
                        start += 1
                        end -= 1
                return result
            return_list = []
            nums.sort()
            for i in range(len(nums)-2):
                value_at_i = nums[i]
                look_for = -value_at_i
                result = twoSum(nums[i+1:], -value_at_i)
                if result:
                    for t in result:
                        t.append(nums[i])
                        t.sort()
                        if t not in return_list:
                            return_list.append(t)
            return return_list
