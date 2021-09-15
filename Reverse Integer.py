class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            x = -x
            neg = True
        y = int(str(x)[::-1])
        
        if neg:
            y = -y
        
        if pow(-2,31) <= -y <= pow(2,31)-1:
            return y
        else: return 0
        
