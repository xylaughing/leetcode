class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-', '')
        s = s.upper()
        groups = int(ceil(len(s) / float(k)))
        ind = len(s) - (groups-1) * k
        res = s[0:ind]
        for i in range(ind, len(s), k):
            res += '-' + s[i: i+k]
        return res
            
