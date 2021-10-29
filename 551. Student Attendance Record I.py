class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        accL, sumA = 0, 0
        for x in s:
            if x == 'P': accL = 0
            elif x == 'A': 
                sumA, accL = sumA + 1, 0
                if sumA >=2: return False
            else: 
                accL += 1
                if accL >= 3: return False
        return True
