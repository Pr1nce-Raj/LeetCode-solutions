class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original=n
        arr=[0,1]
        while n>0:
            arr[0]=arr[0] + (n%10)
            arr[1]=arr[1] *(n%10)
            n=n/10
        if original %(arr[0]+arr[1])!=0:
            return False
        return True
