class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
#        def isprime(n):
#            return (all([False for i in range(2,n) if n % i == 0 ]) and not n < 2)               
#        if isprime(len(s)): 
#             return False

        for i in range(len(s)/2, 0, -1):
            if len(s)%i == 0:
                # duplicates of substring == str return True
                if str(s[0:i]) * (len(s)/i) == s: return True        
        return False
    
