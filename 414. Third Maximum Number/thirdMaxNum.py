class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_set = set(nums)
        result = list(distinct_set)
        result.sort(reverse=True)
        if len(result)>=3:
            return result[2]
        else:
            return max(result)