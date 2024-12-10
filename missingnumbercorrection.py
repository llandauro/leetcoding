def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (len(nums)*(len(nums)+1))/2
    
        for i in range(len(nums)):
            sum = sum - nums[i]

        return sum

# Space complexity of O(1) and time complexity of O(n)