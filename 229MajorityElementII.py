class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1: return nums
        major_dic = collections.Counter(nums)
        res = []
        for x in major_dic.keys():
            if major_dic[x] > len(nums) / 3:
                res.append(x)
        return res
