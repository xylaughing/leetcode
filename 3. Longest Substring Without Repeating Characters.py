class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """"""
        if not s: return 0
        maxs = 1
        for i in range(len(s)):
            if len(s) - i <= maxs: return maxs
            dic, j = s[i:i+maxs], i+maxs
            if len(set(dic)) == len(dic):
                while j < len(s) and s[j] not in dic:
                    dic += s[j]
                    j += 1
                maxs = max(maxs, j - i)
        return maxs
        """
        maxs, l , seen = 0, 0, {}
        for i in range(len(s)):
            if s[i] not in seen:
                maxs = max(maxs, i-l+1)
            else:
                if seen[s[i]] < l:      # s[i] in seen, but outside the window
                    maxs = max(maxs, i-l+1)
                else:                   # s[i] in seen, but in the window.
                    l = seen[s[i]] + 1
            seen[s[i]] = i
        return maxs
