class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums1:
            if x in nums2 and x not in res:
                res.append(x)
            if not nums2: break
        return res
        
        
