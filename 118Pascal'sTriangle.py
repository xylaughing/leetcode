class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def getPascal(arr):
            res = [1]
            if len(arr) >= 2:
                for i in range(len(arr)-1):
                    res.append(arr[i] + arr[i+1])
            res.append(1)
            return res
        
        output, lastarr = [], [1]
        output.append(lastarr) 
        if numRows == 1: return output       
        for i in range(1, numRows):
            temp = getPascal(lastarr)
            output.append(temp)
            lastarr = temp
            
        return output
