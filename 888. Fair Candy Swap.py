class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        """
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        for x in aliceSizes:
            temp = (sumB - sumA)//2 + x
            if temp in bobSizes:
                return [x, temp]
            
        """
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumA - sumB) / 2
        A = sorted(aliceSizes)
        B = sorted(bobSizes)
        i, j = 0, 0
        while i < len(A) and j < len(B):
            temp = A[i] - B[j]
            if temp == diff:
                return [A[i], B[j]]
            elif temp > diff:
                j += 1
            else:
                i += 1
