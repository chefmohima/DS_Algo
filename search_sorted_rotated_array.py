class Solution:
  
    # function to find index of minimum number
    def findMin(self, nums):
        last = nums[-1]
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            # check if minimum
            if nums[mid] <= last and (nums[mid] < nums[mid-1] or mid==0):
                return mid
            else:
                if nums[mid] > last :
                    # in 1st half, move right
                    start = mid+1
                elif nums[mid] < last:
                    # in second half, move left
                    end = mid-1
        return mid
    # function for binary search
    def binary_search(self, nums,key):
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == key:
                return nums[mid]
            elif nums[mid] > key:
                end = mid-1
            else:
                start = mid+1
        return -1
      
    # Actual function for the problem
    def search(self, nums, target):
        if not nums:
            return -1
        # first find index of minimum number
        # we know that arr[:minindex] will be sorted and arr[minindex:] will be sorted
        minindex = self.findMin(nums)
        
        # determine where the target lies? first half or second half and call the binary search on corresponding half
        last = nums[-1]
        if target > last:
            num = self.binary_search(nums[:minindex], target)
        else:
            num = self.binary_search(nums[minindex:], target)
        if num != -1:
            return nums.index(num)
        else:
            return -1
    

