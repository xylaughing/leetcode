class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = len(num) - 1
        carry = k
        while i >= 0 or carry !=0:
            if i >= 0:
                temp = num[i] + carry
            else:
                temp = carry
            carry = int(temp // 10)
            if i >= 0:
                num[i] = temp - carry*10
            else:
                num.insert(0, temp - carry * 10)
            i -= 1        
        return num
        
        
"""        
        arr_k = repr(k)
        carry = 0
        i = len(num) - 1
        j = len(arr_k) - 1
        output = []
        while i>=0 or j >= 0 or carry != 0:
            if i >=0:
                a = num[i] 
            else: a = 0
            if j >= 0:
                b = int(arr_k[j])
            else: b = 0
            print("a=", a, "b=", b)        
            temp = a + b + carry
            carry = temp / 10
            output.insert(0, temp % 10)
            i -= 1
            j -= 1            
        return output
"""            
