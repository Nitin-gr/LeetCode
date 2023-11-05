class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = 1 
        while num <= n:
            if num == n:
                return True
            num *= 2
        return False 


# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n < 1:
#             return False
            
#         while n>1:
#             if n%2 != 0:
#                 return False
#             n //= 2
#         return True