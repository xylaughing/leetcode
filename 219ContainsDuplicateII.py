class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        if k == 0: return False
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            elif i - dic[nums[i]] <= k:
                    return True
            else: dic[nums[i]] = i
        return False
            
