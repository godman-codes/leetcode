class Solution:
    def reverse(self, x: int) -> int:
        number = str(x)[::-1]
        print(number)
        if number[-1] == '-':
            if (int(number[:-1])*-1) < -2147483647:
                return 0
            return int(number[:-1])*-1
        else:
            if int(number) > 2147483647:
                return 0
            return int(number)


print(Solution().reverse(-123))