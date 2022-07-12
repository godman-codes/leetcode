class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        new_list = []
        new_adjacent_list = []
        for i in s:
            if i in new_list:
                new_adjacent_list.append(len(new_list))
                if i == new_list[-1]:
                    new_list = []
                elif i != new_list[-1]:
                    new_list = new_list[new_list.index(i)+1:]
                new_list.append(i)
            else:
                new_list.append(i)
            new_adjacent_list.append(len(new_list))
        return sorted(new_adjacent_list)[-1]
man = Solution()
print(man.lengthOfLongestSubstring("dvdf"))
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         my_set = list(set(s))
#         new_list = []
#         new_adjacent_list = []
#         for i in s:
#             if len(my_set) != len(new_list):
#                 if s.count(i) > 1 and i not in new_list:
#                     new_list.append(i)
#                 elif s.count(i) == 1 and new_adjacent_list == []:
#                     new_list.append(i)
#                     new_adjacent_list.append(i)
#                 elif s.count(i) == 1 and len(new_adjacent_list) == 1:
#                     new_list.append(i)
#             else:
#                 break
#         if new_adjacent_list == []:
#             return len(new_list)
#         elif len(s) == 1:
#             return 1
#         else:
#             new_list.remove(new_adjacent_list[0])
#             return len(new_list)