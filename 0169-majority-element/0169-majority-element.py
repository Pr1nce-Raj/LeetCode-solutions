class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count_dict = Counter(nums)
        
        end_case = len(nums)//2
        for key,value in count_dict.items():
            if value > end_case:return key