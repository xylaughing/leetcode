class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal) or len(s) == 1: return False
        if s == goal:
            return False if len(set(s)) == len(s) else True
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append([s[i], goal[i]])
        if len(diff) != 2: return False
        return True if diff[0] == diff[1][::-1] else False
