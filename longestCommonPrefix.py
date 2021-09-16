class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i] 
            if strs[0][i] != strs[-1][i]:
                break 
        return prefix
