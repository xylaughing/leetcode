class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        """
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return letters[0]        
        """
        
        low, high = 0, len(letters)-1
        while low < high:
            mid = (low + high) // 2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1
        return letters[high] if letters[high] > target else letters[0]
