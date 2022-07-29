class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        symbols = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        def stack_handler():
            if len(myStack) > 1:
                if symbols[myStack[-2]] == myStack[-1]:
                    myStack.pop()
                    myStack.pop()
                elif myStack[-1] in symbols.values() and symbols[myStack[-2]] != myStack[-1]:
                    return False
        for i in s:
            myStack.append(i)
            stack_handler()
        if myStack:
            return False
        return True
                
                
print(Solution().isValid("(((((())))))"))