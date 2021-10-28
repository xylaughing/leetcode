class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return False
        divs, root = 1, int(sqrt(num))       
        while root > 1:
            if num%root == 0:
                divs += root + num/root
            root -= 1
        return divs == num
