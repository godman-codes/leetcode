class Solution:
    new_dict = {
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen',
            '20': 'Twenty',
            '30': 'Thirty',
            '40': 'Forty',
            '50': 'Fifty',
            '60': 'Sixty',
            '70': 'Seventy',
            '80': 'Eighty',
            '90': 'Ninety'
        }
    def less_than_thousands(self, nums: int) -> str:
        sub_solution = []
        hundreds = ((nums%1000)//100)
        tens = (((nums%1000)%100)//10) * 10
        units = ((nums%1000)%100)%10
        if hundreds:
            sub_solution.append(f'{self.new_dict.get(str(hundreds))} Hundred')
        if tens: 
            if tens >= 20:
                sub_solution.append(f'{self.new_dict.get(str(tens))}')
            elif tens == 10:
                sub_solution.append(f'{self.new_dict.get(str(tens + units))}')
        if units:
            if tens >= 20:
                sub_solution.append(f'{self.new_dict.get(str(units))}')
            elif not tens:
                sub_solution.append(f'{self.new_dict.get(str(units))}')
        # return hundreds, tens, units
        return ' '.join(sub_solution)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        new_list = []
        billions = num//1000000000
        millions = (num%1000000000)//1000000
        thousands = ((num%1000000000)%1000000)//1000
        hundreds = ((num%1000000000)%1000000)%1000
        if billions:
            new_list.append(f'{self.less_than_thousands(billions)} Billion')
        if millions:
            new_list.append(f'{self.less_than_thousands(millions)} Million')
        if thousands:
            new_list.append(f'{self.less_than_thousands(thousands)} Thousand')
        if hundreds:
            new_list.append(f'{self.less_than_thousands(hundreds)}')
        return ' '.join(new_list)
man = Solution()
print(man.numberToWords(0))
# man.less_than_thousands(0)
