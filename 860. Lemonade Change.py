class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        c5, c10 = 0, 0
        for x in bills:
            if x == 5:
                c5 += 1
            elif x == 10 and c5 > 0:
                c5 -= 1
                c10 +=1
            elif x == 20:
                if c10 > 0 and c5 > 0:
                    c5, c10 = c5-1, c10-1
                elif c5 > 2:
                    c5 -= 3
                else: return False
            else:
                return False
        return True
