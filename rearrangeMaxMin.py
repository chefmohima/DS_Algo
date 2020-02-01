#Implement a function called maxMin(lst) which will re-arrange the elements of a sorted list
#such that the first position will have the largest number,
#the second will have the smallest, and the third will have second largest, and so on
#Input :  [1,2,3,4,5]
# Output : [5,1,4,2,3]

import pytest

class Solution:
    
    def reArrange(self, sortedList):
        result = []
        i , j = 0, len(sortedList)-1
        while i <= j:
            if i == j:
                # this will be the last element in an odd numbered list
                result.append(sortedList[i])
                break
            else:
                result.append(sortedList[j])
                result.append(sortedList[i])
                i += 1
                j -= 1
        return result
                
    
        
    




class TestSolution:
    def test_rearrange_positivevaluessonly(self):
        s = Solution()
        assert s.reArrange([1,2,3,4,5]) == [5,1,4,2,3]
        
    def test_rearrange_allsamevalues(self):
        s = Solution()
        assert s.reArrange([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
        
    
    def test_rearrange_positiveandnegativevalues(self):
        s = Solution()
        assert s.reArrange([-10, -1, 1, 1, 1, 1]) == [1, -10, 1, -1, 1, 1]
        
    
        
        
        
    