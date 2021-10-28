class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
#        return word.upper() == word or word.lower() == word or word.capitalize() == word

        # faster
        return word.isupper() or word.islower() or word.istitle()
