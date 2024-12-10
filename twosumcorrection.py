def twoSumCorrection(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #create empty Hash table: 
        hash_table = {}
        n = len(nums)

        #build HashSet:
        for i in range(n):
            hash_table[nums[i]] = i # the key is the number and the value is the number's index

        #iterate through all the elements:
        for j in range(n):
            complement = target - nums[j]
            if complement in hash_table and hash_table[complement] != j: 
                return [j, hash_table[complement]]
            else: 
                 hash_table[nums[j]] = j

print(twoSumCorrection([3,2,4], 6))
print(twoSumCorrection([2,7,11,15], 9))
print(twoSumCorrection([3,3], 6))