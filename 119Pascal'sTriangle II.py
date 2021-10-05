class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def getnextPascal(arr):
            output = [1]
            if len(arr) >= 2:
                for i in range(len(arr)-1):
                    output.append(arr[i] + arr[i+1])
            output.append(1)
            return output
            
        lastarr = [1]
        while rowIndex > 0:
            temp = getnextPascal(lastarr)
            lastarr = temp
            rowIndex -= 1
        return lastarr
