import re
class Solution:
    def myAtoi(self, s: str) -> int:
        my_regex = re.compile('(\-|\+)?([0-9])+')
        my_regex2 = re.compile('(\-\+|\+\-|\+\+|\-\-)([0-9])+')
        result = my_regex.search(s)
        result2 = my_regex2.search(s)
        if result != None:
            pointer = s.index(result.group()[0])
            result3 = list(set(s[:pointer]))
            if ' ' in result3:
                result3.remove(' ')
            if result2 != None or len(result3) > 0:
                return 0
        if result == None:
            return 0
        else:
            if int(result.group()) > 2147483647:
                return 2147483647
            elif int(result.group()) < -2147483647:
                return -2147483648
            else:
                return int(result.group())
        

print(Solution().myAtoi('words and +-987'))

# import re

# txt = "The rain in Spain falls mainly in the plain!"

# #Check if the string contains either "falls" or "stays":

# x = re.findall("falls|stays", txt)

# print(x)

# if x:
#     print("Yes, there is at least one match!")
# else:
#      print("No match")
