class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        zeros=0
        for i in range(-1,-m,-1):
            if nums1[i]==0:
                zeros+=1
            else:
                break
        for i in range(zeros):
            if nums1[i]==0:
                nums1.pop(i)
        nums1[m:] = nums2[:n]
        nums1.sort()


# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """

#         for j in range(n):
#           nums1[m+j] = nums2[j]
#         nums1.sort()
        