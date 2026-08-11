class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string=str(x)
        if string[0:]==string[::-1]:
            return True
        else:
            return False