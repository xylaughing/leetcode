class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        # translate string patern to numbers
        def translate(s):
            count, res, dic = 0, "", {}
            for x in s:
                if x not in dic.keys():
                    dic[x] = count
                    res = res + ' ' + str(count)                    
                    count += 1
                else:
                    res = res + ' ' + str(dic[x])
            return res

        return translate(s) == translate(t)        
        
        """
        # compare after each letter    
        ct_s, ct_t, res_s, res_t = 0, 0, 0, 0
        dic_s, dic_t = {}, {}
        for i in range(len(s)):
            if s[i] not in dic_s.keys():
                dic_s[s[i]] = ct_s
                res_s += ct_s                    
                ct_s += 1
            else:
                res_s += dic_s[s[i]]
            if t[i] not in dic_t.keys():
                dic_t[t[i]] = ct_t
                res_t += ct_t
                ct_t += 1
            else:
                res_t += dic_t[t[i]]
            if res_s != res_t:
                return False
        return True
                    
