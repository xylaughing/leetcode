class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = [s[0]]
        start, res = 0, ""
        for i in range(1, len(s)):
            if st:
                if st[-1] == s[i]:
                    st.append(s[i])
                else: 
                    st.pop()
            else:
                res += s[start+1:i-1]
                st.append(s[i])
                start = i
        return res + s[start+1:len(s)-1]
