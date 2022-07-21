class Solution:
    def threeSum(self, nums:int):
        res = []
        nums.sort()
        # loop through a counter and its corresponding values
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                #if the next value is the same as the previous one continue to the next loop
                continue
            else:
                #else do the two sum ii algo
                l,r = i+1,len(nums)-1
                while l < r:
                    cumulative = a + nums[l]+ nums[r]
                    if cumulative > 0:
                        r -= 1
                    elif cumulative < 0:
                        l+=1
                    else:
                        res.append([a, nums[l], nums[r]])
                        l+=1
                        #if the next iteration of l is the same as the previous remove one again 
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
        return res