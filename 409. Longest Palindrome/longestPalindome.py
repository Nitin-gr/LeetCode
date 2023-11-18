class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        result = 0  # Initialize a variable to store the result
        odd = 0

        for val in d.values():
            if val % 2 == 0:
                result += val
            else:
                odd = 1
                result += (val - 1)

        if odd >= 1:
            result += 1

        return result

