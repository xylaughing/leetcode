class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        major_dic = {}
        for x in nums:
            if x in major_dic.keys():
                major_dic[x] += 1
                if major_dic[x] > len(nums) // 2:
                    return x
            else:
                major_dic[x] = 1
        
        
