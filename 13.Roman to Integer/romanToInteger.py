class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        res = 0

        for i in range(len(s)):
            if i < len(s) -1 and m[s[i]] < m[s[i+1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]

        return res
    

# class Solution:
#     def romanToInt(self, s):
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number
        