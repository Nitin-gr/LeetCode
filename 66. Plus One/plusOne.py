class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''.join(map(str,digits))
        istring = int(string) + 1
        lstring = list(str(istring))
        narray = [int(n) for n in lstring]
        return narray 

# class Solution(object):
#     def plusOne(self, digits):
#         for i in range(len(digits) - 1, -1, -1):
#             if(digits[i]!=9):
#                 digits[i]+=1
#                 return digits
#             else:
#                 digits[i] = 0
#         return [1] + digits