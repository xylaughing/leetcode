class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] not in res:
                inserted = False
                for j in range(len(res)):
                    if nums[i] > res[j]: 
                        res.insert(j, nums[i])
                        inserted = True
                        break
                if not inserted: res.append(nums[i])   
                if len(res) > 3: res = res[0:3]
                print("i", i , res)
                
        if len(res) <= 2: return res[0]
        return res[2]
        """
        
        m1, m2, m3 = -float('inf'), -float('inf'), -float('inf')
        for x in nums:
            if x not in [m1, m2, m3]:
                if x > m1: m1, m2, m3 = x, m1, m2
                elif x > m2: m1, m2, m3 = m1, x, m2
                elif x > m3: m1, m2, m3 = m1, m2, x
        
        if m3 == -float('inf'): return m1
        else: return m3
        
