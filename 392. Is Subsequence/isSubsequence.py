class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for i in range(len(t)-2):
        #     if t[i]==s[0]:
        #         if t[i+1]==s[1]:
        #             if t[i+2]==s[2]:
        #                 return True
        #             else:
        #                 i += 1
        #         else:
        #             i += 1 
        #     else:
        #         i += 1 
        # return False     

        i, j = 0, 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i += 1
            j+=1
        return i==len(s)

                 
        