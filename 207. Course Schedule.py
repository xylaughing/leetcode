class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        vec = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for i, j in prerequisites:
            vec[i].append(j)    
        
        def topsort(x):
            if visit[x] == -1:
                return False
            if visit[x] == 1:
                return True
            visit[x] = -1
            for y in vec[x]:
                if not topsort(y):
                    return False
            visit[x] = 1
            return True
            
        for i in range(numCourses):
            if not topsort(i):
                return False
        return True     
