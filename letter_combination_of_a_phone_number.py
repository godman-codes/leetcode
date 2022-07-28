class Solution:
    def letterCombinations(self, digits: str):
        res = []
        digitsToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'qprs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(i, curStr):
            print(curStr, 'curStr')
            print(i, 'i')
            if len(curStr) == len(digits):
                print('if state')
                res.append(curStr)
                print(res)
                return 
            for c in digitsToChar[digits[i]]:
                print(digits[i], 'digit i')
                print(c, 'q')
                backtrack(i+1, curStr+c)
        if digits:
            backtrack(0, '')
        return res

print(Solution().letterCombinations(digits= '23'))