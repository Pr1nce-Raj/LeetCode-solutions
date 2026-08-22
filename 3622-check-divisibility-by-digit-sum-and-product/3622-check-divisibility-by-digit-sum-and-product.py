class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original=n
        dig_sum=0
        dig_prod=1
        while n>0:
            dig_sum=dig_sum + (n%10)
            dig_prod=dig_prod *(n%10)
            n=n/10
        if original %(dig_sum+dig_prod)!=0:
            return False
        return True
