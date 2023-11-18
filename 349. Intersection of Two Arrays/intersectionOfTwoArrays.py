class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        for i in range(len(nums1)):
            if nums1[i] not in d1:
                d1[nums1[i]]=1
            else:
                d1[nums1[i]]+=1
        
        d2 = {}
        for i in range(len(nums2)):
            if nums2[i] not in d2:
                d2[nums2[i]]=1
            else:
                d2[nums2[i]]+=1
        
        l = []
        for key in d1.keys():
            if key in d2:
                l.append(key)
        return l
        