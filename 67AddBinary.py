class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # int to bin with head of "0b"
        temp = bin(int(a, 2) + int(b, 2))
        b_index = temp.index('b')
        return temp[b_index+1:]
