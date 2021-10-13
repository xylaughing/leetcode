class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for x in strs:
            key = tuple(sorted(x))
            dic[key] = dic.get(key,[]) + [x]
        return list(dic.values())
            
