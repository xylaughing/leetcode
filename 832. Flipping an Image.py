class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        m, n = len(image), len(image[0])
        for i in range(m):
            for j in range(n//2):
                image[i][j], image[i][n-1-j] = (1-image[i][n-1-j]), (1-image[i][j])
        
        if n%2 == 1:
            for i in range(m):
                image[i][n//2]= 1- image[i][n//2]
        return image
        """
        return [[1-x for x in IMG[::-1]] for IMG in image]
      
