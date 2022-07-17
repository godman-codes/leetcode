class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        pointer = len(str_x)//2
        if str_x[:pointer] == str_x[::-1][:pointer]:
            return 'true'
        return 'false'

print(Solution().isPalindrome(121))