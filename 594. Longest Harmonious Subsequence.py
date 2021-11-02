class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct = Counter(nums)       
        k, maxs = sorted(ct), 0
        for i in range(len(k)-1):
            if k[i+1] - k[i] == 1:
                maxs = max(ct[k[i+1]] + ct[k[i]], maxs)
        return maxs
