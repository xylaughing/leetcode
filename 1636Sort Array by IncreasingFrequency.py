class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic, res = {}, []
        ct = Counter(nums)
        """
        for x in ct:
            if ct[x] not in dic: 
                dic[ct[x]] = [x]
            else: 
                dic[ct[x]].append(x)
                
        sortedFre = sorted(dic.keys())
        for i in sortedFre:
            for j in sorted(dic[i], reverse = True):
                 res.extend([j] * i)
        return res
        """
    
        return sorted(sorted(nums, reverse=True), key=lambda x: ct[x])
