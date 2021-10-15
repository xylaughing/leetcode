class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ct = Counter(s)
        return ''.join(x * ct[x] for x in sorted(ct, key = lambda x : ct[x], reverse = True))
    
        """
        sorted(ct, key = lambda x : ct[x], reverse = True)
        exp: return a list with ct.keys() ordered by ct.values()
        
        """   
