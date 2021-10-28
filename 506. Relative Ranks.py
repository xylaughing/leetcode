class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """      
        rank = sorted(score, reverse=True)
        dic = dict(zip(rank, ["Gold Medal","Silver Medal", "Bronze Medal"] + list(range(4, len(rank)+1, 1))))
        return [str(dic[x]) for x in score]
