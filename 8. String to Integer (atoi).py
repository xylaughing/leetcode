class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ''
        neg, head = False, False
        for i in range(len(s)):
            #print(i, res)
            if s[i].isnumeric():
                res += s[i]
                head = True
            elif s[i] == ' ':
                if len(res) != 0 or head:
                    break
            elif s[i] == '-':
                if not res and not head:
                    head = True
                    neg = True
                else:
                    break
            elif s[i] == '+':
                if not head: 
                    head = True 
                else: break
            else:
                break
        if not res: return 0
        else:
            if neg:
                return -int(res) if int(res) <= 2**31 else -2**31
            else:
                return int(res) if int(res) < 2**31 else 2**31-1
