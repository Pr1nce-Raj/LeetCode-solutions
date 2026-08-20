class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        check=nums.count(val)
        count=0
        while count<check:
            if val in nums:
                nums.remove(val)
                count+=1
