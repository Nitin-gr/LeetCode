class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        sumNum = 0
        while num>0:
            rem = num%10
            sumNum += rem 
            num //= 10
        
        return self.addDigits(sumNum)   