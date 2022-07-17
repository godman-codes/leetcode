class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        new_dict = []
        pointer = 0
        negative = False
        for i in range(len(s)):
            if i//numRows == 0:
                new_dict.append(s[i])
                pointer += 1
            elif pointer == (numRows):
                new_dict[pointer-2] += s[i]
                negative = True
                pointer -= 1
            elif pointer == 1:
                new_dict[pointer] += s[i]
                negative = False
                pointer += 1
            elif negative:
                new_dict[pointer-2] += s[i]
                pointer -= 1
            elif not negative:
                new_dict[pointer] += s[i]
                pointer += 1
            print(new_dict)
            print(pointer)
            print(negative)
            print(s[i])
                
        return ''.join(new_dict)

man = Solution()
print(man.convert('abc', 1))