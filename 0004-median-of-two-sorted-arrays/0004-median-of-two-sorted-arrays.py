class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result=sorted(nums1+nums2)
        n=len(result)
        if n%2==0:
            median=float(result[n//2] + result[(n//2)-1])/2
        else:
            median = result[len(result)//2]
        return median
        
    