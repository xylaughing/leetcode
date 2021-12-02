class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        def isLeapyear(year):
            if (year % 4) == 0:
                if (year % 100) == 0:
                    if (year % 400) == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        
        y, m, d = int(date[0:4]), int(date[5:7]), int(date[8:10])
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = sum(days[0:m]) + d
        if m > 2 and isLeapyear(y): res += 1
        return res
