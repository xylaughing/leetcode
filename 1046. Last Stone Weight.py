class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        """
        count = [0] * (max(stones) + 1)
        for x in stones:
            count[x] += 1
        
        i, j = len(count)-1, len(count)-1
        while i > 0:
            if count[i]%2 == 0:
                count[i] = 0
                i -= 1
            else:
                j = i-1
                while j > 0 and count[j] == 0:
                    j -= 1
                if j == 0: break
                count[i], count[j] = 0, count[j]-1
                count[i - j] += 1
                i = i - 1
           
        for i in range(len(count)):
            if count[i] != 0:
                return i
        return 0
        """
        
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0] 
