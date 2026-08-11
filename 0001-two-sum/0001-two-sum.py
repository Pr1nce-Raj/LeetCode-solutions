class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store the value and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is already in the map, we found the solution
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the current number and its index
            num_map[num] = i
            
        return []