class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        dic = {}
        for i in range(len(nums2)-1):
            dic[nums2[i]] = -1
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    dic[nums2[i]] = nums2[j]
                    break
        dic[nums2[-1]] = -1
        
        return [dic[x] for x in nums1]
            
