class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dic = {'U':'D', 'R':'L', 'D':'U', 'L':'R'}
        ct = Counter(moves)
        for x in ct.keys():
            if ct[x] != ct[dic[x]]: return False
        return True
            
        
        """ Slower solution
        dic = {'U':'D', 'R':'L', 'D':'U', 'L':'R'}
        openmoves = []
        for x in moves:
            if dic[x] not in openmoves:
                openmoves.append(x)
            else:
                openmoves.remove(dic[x])
        return not openmoves
        
        """
