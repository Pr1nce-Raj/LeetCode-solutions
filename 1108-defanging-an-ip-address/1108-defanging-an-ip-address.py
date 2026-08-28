class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        strings=address.split(".")
        result="[.]".join(strings)
        return result
