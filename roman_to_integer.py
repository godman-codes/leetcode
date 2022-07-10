class Solution:
    def romanToInt(self, s: str) -> int:
        new_list = []
        for i in range(len(s)):
            if s[i] == 'M':
                new_list.append(1000)
            elif s[i] == 'D':
                new_list.append(500)
            elif s[i] == 'C':
                if i != (len(s)-1):
                    if s[i+1] in 'DM':
                        new_list.append(-100)
                    else:
                        new_list.append(100)
                else:
                    new_list.append(100)                
            elif s[i] == 'L':
                new_list.append(50)
            elif s[i] == 'X':
                if i != (len(s)-1):
                    if s[i+1] in 'LCDM':
                        new_list.append(-10)
                    else:
                        new_list.append(10)
                else:
                    new_list.append(10)          
            elif s[i] == 'V':
                new_list.append(5)
            elif s[i] == 'I':
                if i != (len(s)-1):
                    if s[i+1] in 'VXLCDM':
                        new_list.append(-1)
                    else:
                        new_list.append(1)
                else:
                    new_list.append(1)          
        return sum(new_list)
man = Solution()
print(man)
print(man.romanToInt(s='MMMCMXCIX'))
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000