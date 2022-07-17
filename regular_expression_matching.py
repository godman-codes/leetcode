import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        my_regex = re.compile(p)
        results = my_regex.search(s)
        if results != None:
            if results.group() == s:
                return 'true'
        return 'false'

print(Solution().isMatch('aa', 'a'))