class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(x != y for x, y in zip(heights, sorted(heights)))
        
        """
        # count sorting
        count = [0] * (max(heights) + 1)
        for i in range(len(heights)):
            count[heights[i]] += 1
        for i in range(1,len(count)):
            count[i] += count[i-1]

        expected = [0]*len(heights)
        for x in heights:
            expected[count[x]-1] = x 
            count[x] -= 1

        return sum(x != y for x, y in zip(heights, expected))
