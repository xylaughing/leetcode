class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.acu = [0]
        for x in nums:
            self.acu.append(x + self.acu[-1])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.acu[right+1] - self.acu[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
