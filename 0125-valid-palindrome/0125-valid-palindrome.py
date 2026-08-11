class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str="".join(char.lower() for char in s if char.isalnum())
        return new_str==new_str[::-1]
            