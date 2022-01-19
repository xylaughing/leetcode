class Solution(object):
    def helper(self, s, n, path, res):
        if len(s) > n * 3 or len(s) < n:
            return 
        if n == 0 and len(s) == 0:
            res.append('.'.join(path))
            return
        self.helper(s[1:], n-1, path + [s[0]], res)
        if len(s) >= 2 and 9 < int(s[0:2]) < 100:
            self.helper(s[2:], n-1, path + [s[0:2]], res)
        if len(s) >= 3 and 100 <= int(s[0:3]) <= 255:
            self.helper(s[3:], n-1, path + [s[0:3]], res)
            
            
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.helper(s, 4, [], res)
        return res
