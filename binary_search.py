class Solution:
    def search(self, nums, target: int) -> int:
        first =  0
        last = len(nums)-1
        while first <= last:
            mid_point = (first + last)//2
            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] < target:
                first = mid_point + 1
            else:
                last = mid_point - 1

print(Solution().search([-1,0,3,5,9,12], 3))