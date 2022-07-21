class Solution:
    def twoSum(self, numbers, target: int):
        # new_number = numbers[::-1]
        # for i in range(len(numbers)):
        #     remain = target - (numbers[i])
        #     if remain in numbers[i+1:]:
        #         return [i+1, (numbers[i+1:].index(remain) + i + 2)]
        #     if i == len(numbers)//2:
        #         return []
        #     remain = target - (new_number[i])
        #     if remain in new_number[i+1:]:
        #         return [len(new_number) - i, len(new_number) - ((new_number[i+1:].index(remain) + i + 1))][::-1]
        #     if i == len(new_number)//2:
        #         return []

        #faster solution
        l,r = 0, len(numbers)-1

        while l < r:
            cur_target = numbers[l] + numbers[r]
            if cur_target > target:
                r -= 1
            elif cur_target < target:
                l += 1
            else:
                return [l+1, r+1]
        return []


print(Solution().twoSum([2,3,4], 6))