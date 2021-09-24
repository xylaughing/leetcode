class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degree_dict = defaultdict(list)
        for i, num in enumerate(nums):
            degree_dict[num].append(i)

        # find the maxdegree
        maxdegree = 0
        maxdegree_set = set()
        for x in degree_dict:
            cur_deg = len(degree_dict[x])
            if maxdegree < cur_deg:
                maxdegree = cur_deg
                maxdegree_set.clear()
                maxdegree_set.add(x)
            if maxdegree == cur_deg:
                maxdegree_set.add(x)
        
        output = float ('inf')
        for x in maxdegree_set:
            if (degree_dict[x][-1] - degree_dict[x][0] + 1) < output:
                output = degree_dict[x][-1] - degree_dict[x][0] + 1
        return output
        
