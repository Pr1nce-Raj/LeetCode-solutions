class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        indx_z= 0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[indx_z]
                nums[indx_z]=nums[i]
                nums[i]=temp
                indx_z+=1