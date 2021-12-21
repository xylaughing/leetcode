class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        output, temp = [], intervals[0]
        for i in range(1, len(intervals)):
            if temp[0] > intervals[i][0]:
                temp[0] = intervals[i][0]
                temp[1] = max(temp[1], intervals[i][1])
            elif temp[1] >= intervals[i][0]:
                temp[1] = max(temp[1], intervals[i][1])
            else:
                output.append(temp)
                temp = intervals[i]
        output.append(temp)
        return output
                
