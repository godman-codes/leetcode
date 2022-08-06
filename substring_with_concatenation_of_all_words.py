import collections
class Solution:
    def findSubstring(self, s: str, words):
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        print(substring_size, n)
        word_count = collections.Counter(words)
        print(word_count)
        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0
            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j : j + word_length]
                print(sub)
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break
            # Valid if we used all the words
            return words_used == k
        answer = []
        for i in range(n - substring_size + 1):
            print(n-substring_size+1)
            if check(i):
                answer.append(i)
        return answer

print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))


# class Solution:
#     def findSubstring(self, s , words):
#         combinationList = []
#         checker = []
#         result = []
#         if len(words) == 1 and words[0] == s:
#             return [0]
#         def getAllPossibleCombination(words):
#             if len(words) == 1:
#                 sum_comb = ''.join(combinationList + words)
#                 checker.append(sum_comb)
#                 return
#             for i in words:
#                 combinationList.append(i)
#                 newWord = list(words)
#                 newWord.remove(i)
#                 getAllPossibleCombination(newWord)
#                 combinationList.pop()
#         getAllPossibleCombination(words)
#         for i in range(len(s), len(checker[0])):
            
#         return result


# sum_comb = ''.join(combinationList + words)
#                 print(sum_comb)
#                 size = len(sum_comb)-1
#                 print(size)
#                 try:
#                     temp = s.index(sum_comb)
#                     result.append(temp)
#                     while sum_comb in s[temp + size:]:
#                         try:
#                             spot = s[temp + size:].index(sum_comb)
#                             temp = spot+size
#                             result.append(temp)
#                         except ValueError:
#                             break
#                 except ValueError:
#                     pass

# size = len(i)-1
#             try:
#                 temp = s.index(i)
#                 if temp not in result:
#                     result.append(temp)
#                     while i in s[temp + size:]:
#                         try:
#                             spot = s[temp + size:].index(i)
#                             temp = spot+size
#                             result.append(temp)
#                         except ValueError:
#                             break
#             except ValueError:
#                 pass