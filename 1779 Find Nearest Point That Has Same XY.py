class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        dic ={}
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dic[i] = abs(points[i][0] - x) + abs(points[i][1] - y)
        
        if dic: 
            return (sorted(sorted(dic), key = lambda x : dic[x]))[0]
        else: 
            return -1 
