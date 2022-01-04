class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        output, i = [], -1
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                i -= 1
                break
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        return output + [newInterval] + intervals[i+1:]
