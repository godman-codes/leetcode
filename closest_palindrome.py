class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1:
            return str(int(n)-1)
        elif len(n) > 1 and set(n) == {'9'}:
            return str(int(n)+2)
        elif set(n) == {'1', '0'} and '1' not in  n[1:-1]:
            return (len(n)-1)*'9'
        elif n == '11':
            return '9'
        elif n != n[::-1]:
            marker = len(n)
            new_marker = marker//2
            if marker%2:
                matt = f'{n[:new_marker]}{n[new_marker]}{n[:new_marker][::-1]}'
                matt2 = f'{n[:new_marker]}{str(int(n[new_marker])-1)}{n[:new_marker][::-1]}'
                matt3 = f'{n[:new_marker]}{str(int(n[new_marker])+1)}{n[:new_marker][::-1]}'
                if '-' in matt2:
                    return matt
                matt_sum = int(matt) - int(n)
                matt2_sum = int(matt2) - int(n)
                matt3_sum = int(matt3) - int(n)
                if matt_sum < 0:
                    matt_sum*=-1
                if matt2_sum < 0:
                    matt2_sum*=-1
                if matt3_sum < 0:
                    matt3_sum*=-1
                    # if matt_sum <= matt2_sum:
                    #     return matt
                    # elif matt2_sum <= matt3_sum:
                    #     return matt2
                    # else:
                    #     return matt2
                minimum = min(matt_sum, matt2_sum, matt3_sum)
                if minimum == matt_sum and minimum == matt2_sum:
                    return str(min(matt, matt2))
                elif minimum == matt3_sum and minimum == matt2_sum:
                    return str(min(matt2, matt3))
                elif minimum == matt_sum and minimum == matt3_sum:
                    return str(min(matt, matt3))
                elif minimum == matt_sum and minimum == matt3_sum and minimum == matt2_sum:
                    return str(min(matt, matt2, matt3))
                if minimum == matt2_sum:
                    return matt2
                elif minimum == matt_sum:
                    return matt
                elif minimum == matt3_sum:
                        return matt3 
            else:
                if len(n) == 2:
                    
                    return f'{n[:new_marker]}{n[:new_marker][::-1]}'
                else:
                    matt = f'{n[:new_marker]}{n[:new_marker][::-1]}'
                    matt2 = f'{n[:new_marker-1]}{str(int(n[new_marker-1])+1)}{str(int(n[new_marker-1])+1)}{n[:new_marker-1][::-1]}'
                    matt3 = f'{n[:new_marker-1]}{str(int(n[new_marker-1])-1)}{str(int(n[new_marker-1])-1)}{n[:new_marker-1][::-1]}'
                    matt3 = matt3.replace('-', '')
                    matt3 = matt3.replace('_', '')
                    matt_sum = int(matt) - int(n)
                    matt2_sum = int(matt2) - int(n)
                    matt3_sum = int(matt3) - int(n)
                    if matt_sum < 0:
                        matt_sum*=-1
                    if matt2_sum < 0:
                        matt2_sum*=-1
                    if matt3_sum < 0:
                        matt3_sum*=-1
                    minimum = min(matt_sum, matt2_sum, matt3_sum)
                    if minimum == matt_sum and minimum == matt2_sum:
                        return str(min(matt, matt2))
                    elif minimum == matt3_sum and minimum == matt2_sum:
                        return str(min(matt2, matt3))
                    elif minimum == matt_sum and minimum == matt3_sum:
                        return str(min(matt, matt3))
                    elif minimum == matt_sum and minimum == matt3_sum and minimum == matt2_sum:
                        return str(min(matt, matt2, matt3))
                    if minimum == matt2_sum:
                        return matt2
                    elif minimum == matt_sum:
                        return matt
                    elif minimum == matt3_sum:
                        return matt3 
        elif n == n[::-1]:
            marker = len(n)
            new_marker = marker//2
            if marker%2:
                if int(n[new_marker]) > 0:
                    return f'{n[:new_marker]}{str(int(n[new_marker])-1)}{n[new_marker+1:]}'
                else:
                    return f'{n[:new_marker]}{str(int(n[new_marker])+1)}{n[new_marker+1:]}'
            else:
                if marker > 3:
                    if int(n[new_marker]) > 0:
                        return f'{n[:new_marker-1]}{str(int(n[new_marker-1])-1)}{str(int(n[new_marker])-1)}{n[new_marker+1:]}'
                    else:
                        if len(n) == 4 and int(n[0]) > 1:
                            return f'{int(n[0])-1}{9}{9}{int(n[-1])-1}'
                        return f'{n[:new_marker-1]}{str(int(n[new_marker-1])+1)}{str(int(n[new_marker])+1)}{n[new_marker+1:]}'
                else:
                    return f'{str(int(n[new_marker-1])-1)}{str(int(n[new_marker])-1)}'

n = Solution()
print(n.nearestPalindromic("500"))