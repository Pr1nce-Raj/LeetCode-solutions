class Solution(object):
    def removeElement(self, nums, val):
        ptr = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr] = nums[i]
                if i != ptr:
                    nums[i] = 0 
                ptr += 1
        return ptr