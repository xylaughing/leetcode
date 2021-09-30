class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # min_cost of i = min(min_cost of i-2, min_cost of i-1) + cost[i]
        
        min_cost = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            min_cost.append(min(min_cost[i-2], min_cost[i-1]) + cost[i])
        return min(min_cost[-1], min_cost[-2])
