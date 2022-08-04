class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            if dividend > 2147483647:
                return 2147483647
            elif dividend < -2147483648:
                return -2147483648
            return dividend
        negative_dividend = False
        negative_divisor = False
        new_divisor =  divisor
        new_dividend =  str(dividend)
        if dividend < 0:
            negative_dividend = True
            new_dividend = new_dividend[1:]
        if divisor < 0:
            negative_divisor = True
            new_divisor = int(str(divisor)[1:])
        remainder = 0
        result = ''
        for i in new_dividend:
            count = 0
            if remainder:
                temp_i = int(str(remainder) + i)
            else:
                temp_i = int(i)
            while True:
                if temp_i >= new_divisor:
                    temp_i -= new_divisor
                    count += 1
                else:
                    remainder = temp_i
                    break
            result += str(count)
        if (negative_divisor and negative_dividend) or (not negative_dividend and not negative_divisor):
            final_result = int(result)
            if final_result > 2147483647:
                return 2147483647
            return final_result
        elif negative_dividend or negative_divisor:
            final_result = int(result)*-1
            if final_result < -2147483648:
                return -2147483648
            return final_result
print(Solution().divide(-9999999999999,10))