class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        """
        lets, digs = {}, []
        for log in logs:
            if log.split(" ", 1)[1][0].isnumeric():
                digs.append(log)
            else:
                log = log.split(" ", 1)
                if lets.has_key(log[1]):
                    lets[log[1]].append(log[0])
                else:
                    lets[log[1]] = [log[0]]
    
        res = []
        for x in sorted(lets):
            for y in sorted(lets[x]):
                res.append(y + " " + x)
        return res + digs
        """
        
        def sort(log):
            x, y = log.split(" ", 1)
            if y[0].isnumeric():
                return (1, None, None)
            else:
                return (0, y, x)
        return sorted(logs, key=sort)
