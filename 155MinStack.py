class MinStack(object):

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.minstack) == 0 or val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        temp = self.stack.pop()
        if temp == self.minstack[-1]:
            self.minstack.pop()
      
    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1]  

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]   
        
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
