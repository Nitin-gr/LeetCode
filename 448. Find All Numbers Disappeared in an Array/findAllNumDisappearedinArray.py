class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

    
        result = []
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        for i in range(1,len(nums)+1):
            if i not in d:
                result.append(i)
            
        return result
