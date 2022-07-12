class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            second_target = (target) - (nums[i])
            if (second_target) in nums[:i]:
                return [i, (nums.index(second_target))]
            elif (second_target) in nums[i+1:]:
                return [i, (nums[i+1:].index(second_target))+len(nums[:i+1])]
            
