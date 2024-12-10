def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = 0
        num_list = []
        for number1 in nums:
            print("number 1 is " + str(number1) + " at index " + str(index1))
            for number2 in nums: 
                if index1 != index2:
                    print("number 2 is " + str(number2) + " at index " + str(index2))
                    sum = number1 + number2
                    if (sum) == target:
                        print("sum of the two numbers is " + str(sum) + " at indexes " + str(index1) + " and " + str(index2))
                        num_list = [index1, index2]
                        return num_list
                index2 += 1
            index2 = 0
            index1 += 1

twoSum([3,2,4], 6)