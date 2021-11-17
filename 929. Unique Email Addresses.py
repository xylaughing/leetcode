class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = 0
        dic = []
        for email in emails:
            temp = email.split('@')
            name = temp[0].split('+')[0].replace(".", "") + "@" + temp[1]
            if name not in dic:
                dic.append(name)
        return len(dic)
