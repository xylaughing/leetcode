class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_dic = collections.Counter(s)
        t_dic = collections.Counter(t)
        return s_dic == t_dic
    
    
        """
        for x in s_dic.keys():
            if x not in t_dic.keys():
                return False
            elif s_dic[x] != t_dic[x]:
                return False
            else:
                del t_dic[x]
        if len(t_dic.keys()) != 0: return False
        else: return True       
        
        """
