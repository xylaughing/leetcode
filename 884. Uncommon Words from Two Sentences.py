class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """"""
        s1, s2 = s1.split(), s2.split()
        c1, c2 = Counter(s1), Counter(s2)
        return [i for i in c1 if c1[i] == 1 and i not in c2] + [i for i in c2 if c2[i] == 1 and i not in c1]
        """
        c = Counter((s1 + " " + s2).split())
        return [x for x in c if c[x] == 1]
