    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """      
        stack = []
        mapping = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c in mapping:
                if stack and mapping[c] == stack[-1]:
                    stack.pop()
                else: return False                
            else: 
                stack.append(c)              
        
        if len(stack) == 0:
            return True
        else:
            return False
