class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        text = re.findall(r'[balloon]', text)
        ct = Counter(text)
        if len(ct.keys()) != 5: 
            return 0
        if ct.has_key('l') and ct.has_key('o'):
            ct['l'] = ct['l'] // 2
            ct['o'] = ct['o'] // 2
        else:
            return 0
        return ct[sorted(ct, key = lambda x : ct[x])[0]]
