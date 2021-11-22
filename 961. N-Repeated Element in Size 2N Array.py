class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ct = Counter(nums)
        return [x for x in ct.keys() if ct[x] == len(nums)//2][0]
        """
        
        return (sum(nums) - sum(set(nums))) / (len(nums)//2 - 1)    
