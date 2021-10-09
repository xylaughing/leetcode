class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
    
        def bitToNum(n):
            if n == 0: return [0]
            if n == 1: return [1, 2, 4, 8, 16, 32]
            output = []            
            source = bitToNum(n-1)
            for x in source:
                if x%2 == 0 and x+1 < 60: output.append(x+1)
            for x in output:
                if 2*x not in output and 2*x < 60: output.append(2*x)
            output.sort()
            return output
        
        res = []
        for h_bits in range(0, turnedOn+1):
            m_bits = turnedOn - h_bits
            h_list = [x for x in bitToNum(h_bits) if x <12]
            m_list = bitToNum(m_bits)
            for i in range(len(h_list)):
                for j in range(len(m_list)):
                    if m_list[j] < 10: res.append(str(h_list[i]) + ":0" + str(m_list[j]))
                    else: res.append(str(h_list[i]) + ":" + str(m_list[j]))
        return res
                 
