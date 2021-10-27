class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i] + duration > timeSeries[i+1]:
                total += timeSeries[i+1] - timeSeries[i]
            else:
                total += duration
        
        return total + duration
