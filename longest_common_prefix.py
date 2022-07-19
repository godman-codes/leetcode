class Solution:
    # def reducer(self, shortest, strs, str_len,)
    def longestCommonPrefix(self, strs) -> str:
        longest = ''
        str_len = len(strs)
        for i in range(str_len):
            if i == 0:
                longest = strs[i]
            else:
                if len(longest) >= len(strs[i]):
                    longest = longest[:len(strs[i])]
                    found = False
                    while not found:
                        if longest != strs[i][:len(longest)]:
                            longest = longest[:-1]
                            if longest == '':
                                return ''
                        elif longest == strs[i][:len(longest)]:
                            found = True
                else:
                    found = False
                    while not found:
                        if longest != strs[i][:len(longest)]:
                            longest = longest[:-1]
                            if longest == '':
                                return ''
                        elif longest == strs[i][:len(longest)]:
                            found = True
        return longest

print(Solution().longestCommonPrefix(["flower","flow","floight"]))



            # while (i + 1) < str_len and not found:
            #     elif len(longest) > len[strs[i]]:
            #         longest = 





                
                # if len(longest) > 0:
                #     shortest = longest
                #     if strs[i+1][:len(shortest)] != shortest:
                #         shortest = shortest[:-1]
                #     elif strs[i+1][:len(shortest)] == shortest:
                #         longest = strs[i+1][:len(shortest)]
                #         found = True
                #         break
                # if len(strs[i]) <= len(strs[i+1]):
                #     if len(shortest) == 0:
                #         shortest = strs[i]
                #     if strs[i+1][:len(shortest)] != shortest:
                #         shortest = shortest[:-1]
                #     else:
                #         longest = strs[i+1][:len(shortest)]
                #         found = True