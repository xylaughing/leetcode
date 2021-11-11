class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def isOverlap(rec1x1, rec1x2, rec2x1, rec2x2):
            if rec1x1 <= rec2x1 and rec1x2 > rec2x1:
                return True
            elif rec1x1 >= rec2x1 and rec1x1 < rec2x2:
                return True
            return False
        return isOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) and isOverlap(rec1[1], rec1[3], rec2[1], rec2[3])
        
        """
        # left = max(rec1[0], rec2[0])
        # right = min(rec1[2], rec2[2])
        # bottom = max(rec1[1], rec2[1])
        # up = min(rec1[3], rec2[3])
        # return left < right and bottom < up
        return max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]) and max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        """
