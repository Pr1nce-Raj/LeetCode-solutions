import java.util.HashSet;
import java.util.Set;

class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        int target = 1;
        while (numSet.contains(target)) {
            target++;
        }
        
        return target;
    }
}