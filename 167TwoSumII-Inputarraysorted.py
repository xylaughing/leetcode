class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) == 2: return [1,2]
        
        sPointer, bPointer = 0, len(numbers)-1
        while sPointer < bPointer:
            if numbers[sPointer] + numbers[bPointer] == target:
                return [sPointer+1, bPointer+1]
            elif numbers[sPointer] + numbers[bPointer] > target:
                bPointer -= 1
            else: sPointer += 1
            
