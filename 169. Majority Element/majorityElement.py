class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ndict = {}

        for i in range(len(nums)):
            if nums[i] not in ndict:
                ndict[nums[i]] = 1
            else:
                ndict[nums[i]] += 1

        return max(ndict, key=ndict.get)