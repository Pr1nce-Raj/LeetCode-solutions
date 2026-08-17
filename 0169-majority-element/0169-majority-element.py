class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        uniq_num = 0
        for curr_num in nums :
            if count==0:
                uniq_num=curr_num
            if uniq_num==curr_num:
                count+=1
            else:
                count-=1
        return uniq_num