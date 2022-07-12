class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort(reverse=True)
        if len(nums1) % 2:
            return nums1[len(nums1)//2]
        else:
            return (nums1[(len(nums1)//2)-1] + nums1[(len(nums1)//2)])/2


man = Solution()
print(man.findMedianSortedArrays([1,2],[3,4]))