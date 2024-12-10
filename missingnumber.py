def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = set()

        #Initialize the Hash Set
        for i in range(len(nums)):
            hash_set.add(nums[i])

        for i in range(len(nums) + 1):
            if i not in hash_set:
                return i
            
print(missingNumber([0,1,3]))
#Time complexity of O(n) and space complexity of O(1)