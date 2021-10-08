class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        output = 0
        for i in range(32):
            output <<= 1
            output = output | (n&1)
            n >>= 1    
        return output
