class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        meaning = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum=0
        previous=0
        for i in range(len(s)-1,-1,-1):
            current = meaning[s[i]]
            if current < previous:
                sum-=meaning[s[i]]
            else:
                sum+=meaning[s[i]]
            previous=current
        return sum         