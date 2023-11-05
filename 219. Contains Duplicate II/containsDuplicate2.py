class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d and i-d[n]<=k: return True
            d[n] = i
        return False

#time limit exceeded
#  class Solution(object):
#      def containsNearbyDuplicate(self, nums, k):
#          """
#          :type nums: List[int]
#          :type k: int
#          :rtype: bool
#          """
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j] and abs(i-j)<=k:
#                     return True
#         return False

        