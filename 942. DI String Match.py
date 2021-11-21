class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res = [0]
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == "I":
                right += 1
                res.append(right)
            else:
                left -= 1
                res.append(left)
        return [x - left for x in res]
