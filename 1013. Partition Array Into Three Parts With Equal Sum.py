class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        sums = sum(arr)
        if sums % 3 != 0: return False 
        acc, partion = 0, 0
        for i in range(len(arr)):
            acc += arr[i]
            if acc == sums//3:
                partion += 1
                acc = 0
        if acc == sums//3: partion += 1
        return True if partion >= 3 else False
                
