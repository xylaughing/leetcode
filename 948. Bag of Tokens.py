class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        if not tokens: return 0
        tokens = sorted(tokens)
        i, j = 0, len(tokens)-1
        score = 0
        while i < j and power >= 0:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return score+1 if power >= tokens[i] else score
            
