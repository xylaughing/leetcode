class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        res = []
        vowels= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sentence = sentence.split()
        for i in range(len(sentence)):
            w = sentence[i]
            if w[0] in vowels:
                w += 'ma' + 'a'*(i+1)
            else:
                w = w[1:] + w[0] + 'ma' + 'a'*(i+1)
            res.append(w)
        return ' '.join(res)
