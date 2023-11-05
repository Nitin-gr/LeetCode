class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def square(n):
            rem = 0
            sq = 0
            while n > 0:
                rem = n % 10
                sq += rem * rem
                n = n//10 
            return sq
    
        sums = set()

        while(n != 1):

            n = square(n)

            if n in sums:
                return False
            
            sums.add(n)
        
        return True
