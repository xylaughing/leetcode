class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        """
        i, j, prev = 0, 0, -1
        while i < len(name) and j < len(typed):
                if name[i] == typed[j]:
                    prev = name[i]
                    i, j = i+1, j+1
                elif name[i] != typed[j] and prev == typed[j]:
                    j += 1
                else:
                    return False
        while j < len(typed):
            if typed[j] == name[-1]:
                j += 1
            else:
                return False
        return True if i == len(name) and j == len(typed) else False
        """
