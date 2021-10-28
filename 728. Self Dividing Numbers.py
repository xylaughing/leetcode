class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isValid(num):
            for x in str(num):
                if int(x) == 0 or num%int(x) != 0: return False
            return True
        
        return [x for x in range(left, right+1) if isValid(x)]
