class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res_match = []
        i, j, minIndexSum = 0, 0, len(list1)+len(list2)-2
        for i in range(len(list1)):
            for j in range(min(len(list2), minIndexSum - i + 1)):
                if list1[i] == list2[j]:
                    if i + j < minIndexSum:
                        res_match = []
                        res_match.append(list1[i])
                        minIndexSum = i + j
                    elif i + j == minIndexSum:
                        res_match.append(list1[i])
        
        return res_match
           
