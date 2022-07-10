class Solution:
    def check_hundred(self, hundreds):
        if hundreds == 9:
            return 'CM'
        elif hundreds == 8:
            return 'DCCC'
        elif hundreds == 7:
            return 'DCC'
        elif hundreds == 6:
            return 'DC'
        elif hundreds == 5:
            return'D'
        elif hundreds == 4:
            return'CD'
        else:
            return hundreds*'C'
    def check_tens(self, tens):
        if tens == 9:
            return 'XC'
        elif tens == 8:
            return 'LXXX'
        elif tens == 7:
            return 'LXX'
        elif tens == 6:
            return 'LX'
        elif tens == 5:
            return'L'
        elif tens == 4:
            return'XL'
        else:
            return tens*'X'
    def check_units(self, units):
        if units == 9:
            return 'IX'
        elif units == 8:
            return 'VIII'
        elif units == 7:
            return 'VII'
        elif units == 6:
            return 'VI'
        elif units == 5:
            return'V'
        elif units == 4:
            return'IV'
        else:
            return units*'I'
    def intToRoman(self, num: int) -> str:
        answer = ''
        {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
        '   X': 10,
        'V': 5,
        'I': 1,
        'IX': 9,
        'XC': 90,
        'CM': 900
        }
        thousands = (num//1000)
        hundreds = ((num%1000)//100) 
        tens = (((num%1000)%100)//10)
        units = ((num%1000)%100)%10
        if thousands:
            answer =+ thousands * 'M'
        if hundreds:
            answer += self.check_hundred(hundreds)
        if tens:
            answer += self.check_tens(tens)
        if units:
            answer+= self.check_units(units)
        return answer

man = Solution()
print(man.intToRoman(1994))
