class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        """
        res, stack = [], ""
        for i in range(len(path)):
            if path[i] == '/' and stack:
                if stack == "/..":
                    if res:
                        res.pop()
                elif stack != '/.' and stack != '/':             
                    res.append(stack)
                stack = '/'
            else:
                stack += path[i]
        if stack not in ['/..', '/.', '/']: 
            res.append(stack)
        elif stack == '/..' and res:
            res.pop()
        return "".join(res) if res else '/'
        """
        
        res = []
        for x in path.split('/'):
            if x == '..':
                if res: res.pop()
            elif x != '' and x!='.':
                res.append(x)
        return '/' + '/'.join(res)
