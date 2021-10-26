class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        R, C = len(image), len(image[0])
        origColor = image[sr][sc]
        def check(r, c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            if image[r][c] != origColor or image[r][c] == newColor:
                return
            image[r][c] = newColor
            check(r-1, c)
            check(r+1, c)
            check(r, c-1)
            check(r, c+1)
        
        check(sr, sc)
        return image
