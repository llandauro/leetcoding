def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

    array = [0] * (n+1) 

    for i in range(n):
            if i == 1 or i == 0: 
                array[i] = 1
            else: 
                array[i] = array[i-1] + array[i-2]

    return array[n]

print(climbStairs(2))