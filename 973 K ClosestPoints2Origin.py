class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dic = {}
        for i, j in enumerate(points):
            dic[i] = j[0]**2 + j[1]**2
            
        return [points[i] for i in sorted(dic, key = lambda x : dic[x])[0:k]]
            
