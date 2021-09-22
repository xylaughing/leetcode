# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def binarysearchVer(l, r):
            if l > r:
                return l
            else:
                mid = (r + l) // 2
                if isBadVersion(mid):
                    return binarysearchVer(l, mid-1)
                else:
                    return binarysearchVer(mid+1, r)
            
        return binarysearchVer(0, n) 
