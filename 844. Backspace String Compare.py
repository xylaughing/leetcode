class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        def finalstr(s):
            res = []
            for x in s:
                if x == '#': 
                    if res: res.pop()
                else: 
                    res.append(x)
            return res
        return finalstr(s) == finalstr(t)
        """
        i = j = countS = countT = 0
        s, t = s[::-1], t[::-1]
        while i < len(s) or j < len(t):
            while i < len(s):
                if s[i] == '#':
                    countS += 1
                    i += 1
                elif s[i] != '#' and countS > 0:
                    i += 1
                    countS -= 1
                else:   break
            while j < len(t):
                if t[j] == '#':
                    countT += 1
                    j += 1
                elif t[j] != '#' and countT > 0:
                    j += 1
                    countT -= 1
                else:   break
            if (i >= len(s) and j < len(t)) or (i < len(s) and j >= len(t)):
                return False
            if i < len(s) and j < len(t) and s[i] != t[j]:
                return False            
            i, j = i+1, j+1
        return True    
