class Solution:
    def removeElement(self, nums, val: int) -> int:
        l = len(nums)-1
        p = 0
        while p < l:
            if nums[p] == val:
                while p < l:
                    if nums[l] != val:
                        nums[p] = nums[l]
                        nums[l] = val
                        break
                    else:
                        l-=1
                    if p == l:
                        return p
            p+=1
        if len(nums) == 0 or nums[0] == val:
            return 0
        if val not in nums:
            return len(nums)
        return p
print(Solution().removeElement([2,2,3], 2))
        