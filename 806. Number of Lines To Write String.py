class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        result=[1, 0]
        for x in s:
            if result[1] + widths[ord(x)-ord('a')] > 100:
                result[0] += 1
                result[1] = 0
            result[1] += widths[ord(x) - ord('a')]
        return result
