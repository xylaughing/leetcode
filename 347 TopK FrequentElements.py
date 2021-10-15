class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct = Counter(nums)
        return sorted(ct, key = lambda x : ct[x], reverse = True)[0:k]
