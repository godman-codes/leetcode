class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        try:
            return haystack.index(needle)
        except ValueError:
            return -1
        