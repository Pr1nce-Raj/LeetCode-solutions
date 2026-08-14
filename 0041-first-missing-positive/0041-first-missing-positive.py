class Solution(object):
    def firstMissingPositive(self, nums):
        sor_list = sorted(list(set(nums)))
        
        target = 1
        
        for val in sor_list:
            if val <= 0:
                continue
            
            if val == target:
                target += 1
            elif val > target:
                return target
                
        return target