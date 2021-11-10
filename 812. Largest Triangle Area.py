class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # Let a,b,c be the lengths of the sides of a triangle. The area is given by:
        # Area = sqrt( p (p−a)(p−b)(p−c) )    
        # where p is half the perimeter,  (a+b+c)/ 2
        def getSide(p1, p2):
            return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        
        def getArea(s1, s2, s3):
            if s1 < s2 + s3 and s2 < s1+s3 and s3 < s1+s2:
                p = (s1 + s2 + s3) / 2
                return  sqrt(p * (p-s1) * (p-s2) * (p-s3))
        
        maxarea = 0
        maxp = 0
        for i in range(len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    s1, s2, s3 = getSide(points[i], points[j]), getSide(points[j], points[k]), getSide(points[i], points[k])
                    maxarea = max(maxarea, getArea(s1,s2,s3))            
        return maxarea
