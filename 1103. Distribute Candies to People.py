class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        ct = int((-1 + sqrt(1 + 4*2*candies)) / 2)
        last = candies - (1+ct)*ct//2
        for i in range(ct):
            res[i%num_people] += i+1
        res[ct % num_people] += last      
        return res
