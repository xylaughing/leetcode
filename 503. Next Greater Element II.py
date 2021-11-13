class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """    
        st, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            # top of st is the smallest in the st. if cur larger than the top of st should pop out
            while st and nums[st[-1]] < nums[i]:
                res[st.pop()] = nums[i]
            st.append(i)
        return re
