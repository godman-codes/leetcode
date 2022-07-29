class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        parenthesis = ['{}', '[]', '()']
        def stack_handler():
            if len(myStack) > 1:
                temp = myStack[-2] + myStack[-1]
                print(temp)
                while temp in parenthesis:
                    myStack.pop()
                    myStack.pop()
                    if len(myStack) > 1:
                        temp = myStack[-2] + myStack[-1]
                    else:
                        temp = 1
            return
        for i in s:
            myStack.append(i)
            stack_handler()
        if myStack:
            return False
        return True
                
                
print(Solution().isValid("(]"))