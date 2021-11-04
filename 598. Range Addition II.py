class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        
        if not ops: return m * n
#        minx = min([ops[i][0] for i in range(len(ops))])
#        miny = min([ops[i][1] for i in range(len(ops))])
        return min([ops[i][0] for i in range(len(ops))]) * min([ops[i][1] for i in range(len(ops))])
