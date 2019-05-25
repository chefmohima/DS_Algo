# Given an array of  integers, find a subarray that sums to a given number X
# optimized soln O(N)
def subarray_sum(l,X):
    l[-1] = 0
    i = 0
    d = dict()  # maintain a dictionary with each cumulative sum as key and its index as value
	# calculate cumulative sum at index A[i] = A[0]+...+A[i-1]
    
	curr_sum = 0   # cumulative sum at each index
    while i < len(l):
        curr_sum = curr_sum + l[i]
		
        if curr_sum == X:
            return 0,i
        elif curr_sum-X in d:
            return d[curr_sum-X] + 1, i
        else:
            d[curr_sum] = i
        i += 1
            
    return None
    
l = [4,5,-2,6,9,10,-1]
subarray_sum(l,3)

# Given an array of positive integers, find a subarray that sums to a given number X
# brute-force soln O(n*n)
def subarray_sum(nums, n):
        """
        :type nums: List[int]
        :rtype: int
        O(N*2)
        """
        
        for i in range(len(nums)):
            sum = nums[i]
            for j in range(i+1,len(nums)):
                sum += nums[j]
                if sum == n:
                    return i,j
        return None
        
l = [0,1,5,3,4,2,10]
subarray_sum(l,12)