class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs, l, score = 0, 0, 0
        seen = {}
        for i in range(len(nums)):
            while nums[i] in seen:
                score -= nums[l]
                del seen[nums[l]]
                l += 1
            seen[nums[i]] = i
            score += nums[i]
            maxs = max(maxs, score)
        return maxs
