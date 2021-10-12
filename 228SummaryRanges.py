class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        
        page = [nums[0]]
        output = []
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] != 1:
                page.append(nums[i-1])
                if page[0] == page[1]:
                    output.append(str(page[0]))
                else:
                    output.append(str(page[0]) + "->" + str(page[1]))
                page = [nums[i]]
                
        if len(page) > 0:
            if page[0] != nums[-1]:
                output.append(str(page[0]) + "->" + str(nums[-1]))
            else: output.append(str(page[0]))
        return output
    
             
