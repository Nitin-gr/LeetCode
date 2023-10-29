class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        nums = s[::-1]
        if x >= 0:
            return int(nums) == x
        else:
            return False