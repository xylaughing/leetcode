class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letters = Counter([x.lower() for x in licensePlate if x.isalpha()])
        # if word contain all letters, letters-Counter(word) is empty
        return min([word for word in words if not(letters-Counter(word))], key = len)
