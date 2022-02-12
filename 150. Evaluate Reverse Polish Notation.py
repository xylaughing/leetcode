class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        i = 1
        for x in tokens:
            if x not in "+-*/":
                stack.append(int(x))
            else:
                a, b = stack.pop(), stack.pop()
                if x == '+':
                    stack.append(b + a)
                elif x == '-':
                    stack.append(b - a)
                elif x == '*':
                    stack.append(b * a)
                else:
                    stack.append(int(float(b) / a))
        return stack[0]
