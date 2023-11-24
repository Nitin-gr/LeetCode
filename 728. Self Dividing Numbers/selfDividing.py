class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def divisible(n):
            for j in str(n):
                if j == '0' or n%int(j) > 0:
                    return False
            return True

        result = []
        for i in range(left,right+1):
            if divisible(i):
                result.append(i)
        return result