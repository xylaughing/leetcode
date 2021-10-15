class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ct = Counter(words)
        return sorted(sorted(ct), key = lambda x : ct[x], reverse = True)[0:k]
