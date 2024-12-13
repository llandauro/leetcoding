class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # First think of the length of both words !!
        if len(s) != len(t):
            return False

        dictionary = {}

        for letter in s:
            if letter not in dictionary: 
                dictionary[letter] = 1
            else: 
                dictionary[letter] += 1

        for letter in t:
            if letter not in dictionary: 
                return False
            else:
                dictionary[letter] -= 1
                if dictionary[letter] < 0: 
                    return False
            
        for letter in dictionary: 
            if dictionary[letter] != 0: 
                return False

        return True
      
print(Solution().isAnagram("anagram", "nagaram"))