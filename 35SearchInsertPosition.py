class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarysearch(nums, l, r, x):
            if r < l:
                return l
            else:
                mid = (r + l) // 2
                print("mid = ", mid)
                if x == nums[mid]:
                    return mid
                else:
                    if x > nums[mid]:
                        return binarysearch(nums, mid+1, r, x)
                    else: return binarysearch(nums, l, mid-1, x)
                     
        return binarysearch(nums, 0, len(nums)-1, target)
