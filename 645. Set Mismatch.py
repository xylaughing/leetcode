class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        ct = Counter(nums)
        return [x for x in ct.keys() if ct[x]>1] + [x for x in range(1, len(nums)+1) if not ct.has_key(x)]
        """

        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]
