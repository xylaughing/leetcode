class Solution(object):
    import re
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # re.finall() better than re.sub()
        para = re.findall(r'\w+', paragraph.lower())
        if not banned: return para[0]
        ct = Counter(para)
        ct = sorted(ct, key = lambda x : ct[x], reverse = True)
        for x in ct:
            if x not in banned:
                return x
        
