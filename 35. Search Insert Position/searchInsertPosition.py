class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    return i

# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         low = 0
#         high = len(nums) - 1
#         ans = len(nums)
#         while(low <= high):
#             mid = (low + high) // 2
#             if nums[mid] >= target:
#                 ans = mid
#                 high = mid -1
#             else:
#                 low = mid + 1
#         return ans 