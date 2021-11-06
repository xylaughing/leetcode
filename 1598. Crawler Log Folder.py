class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        res = 0
        for x in logs:
            if x == '../':
                res = res - 1 if res else 0
            elif x == './':
                continue
            else:
                res += 1
        return res
