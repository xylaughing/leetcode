class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if not b: return 0

        start = int(ceil(float(len(b))/len(a)))
        for i in range(start, start+2, 1):
            if b in a*i: 
                return i
        return -1
        
