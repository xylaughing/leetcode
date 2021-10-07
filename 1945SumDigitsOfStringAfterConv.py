class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """               
        dic = dict.fromkeys(['a', 'j'], 1)
        dic.update(dict.fromkeys(['b', 'k', 't'], 2))
        dic.update(dict.fromkeys(['c', 'l', 'u'], 3))       
        dic.update(dict.fromkeys(['d', 'm', 'v'], 4))   
        dic.update(dict.fromkeys(['e', 'n', 'w'], 5))   
        dic.update(dict.fromkeys(['f', 'o', 'x'], 6))   
        dic.update(dict.fromkeys(['g', 'p', 'y'], 7))  
        dic.update(dict.fromkeys(['h', 'q', 'z'], 8))   
        dic.update(dict.fromkeys(['i', 'r'], 9))  
        dic['s'] = 10
                   
        sumdig = 0
        for x in s: sumdig += dic[x]  
        if k ==1: return sumdig
        
        while k > 1 and sumdig >= 10:
            temps = 0
            while sumdig > 0:
                temps += sumdig%10
                sumdig = sumdig // 10
            k -= 1
            sumdig = temps
        return sumdig
