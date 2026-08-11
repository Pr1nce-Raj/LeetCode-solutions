class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        split_string= (s.strip()).split(" ")
        last_element =split_string[-1]
        return len(last_element)
        