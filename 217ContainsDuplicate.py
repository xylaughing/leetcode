class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = collections.Counter(nums)
        for x in dic.values():
            if x != 1: return True
        return False
    
    # return [True for x in dic.values() if x != 1]
