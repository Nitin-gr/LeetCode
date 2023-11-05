class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        while n%2==0: n/=2
        while n%3==0: n/=3
        while n%5==0: n/=5
        return n==1

# class Solution(object):
#     def isUgly(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         while n>1:
#             if n%5 ==0:
#                 n/=5
#             elif n%3==0:
#                 n/=3
#             elif n%2==0:
#                 n/=2
#             else:
#                 return False
#         return n==1
            