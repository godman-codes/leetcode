class Solution:
    def maxArea(self, height) -> int:
        
        res = 0
        l = 0
        r = len(height)-1
        while l < r:
            temp_width = r-l
            temp_height = min(height[l], height[r])
            if (temp_height * temp_width) > res:
                res = temp_height * temp_width
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            print(l,r)
        return res

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))