#given a roman numeral, convert it to an integer. INput will be from 1 to 3999

#Read through string
# look at current letter and next letter
# for letter in dictionary.index()
# if key(current letter) < key(next letter) #e.g. I is < V
#     integer = key(next) - key(current)
#     sum += integer
#     skip next letter
# else
#     integer = key(current)
#     sum += integer

class Solution:
    def romanToInt(self, roman):
        table = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        sum = 0
        i = 0
        # print(len(roman))
        while i < len(roman):
            # print(i)
            if i == len(roman)-1:
                adder = table[roman[i]]
                sum += adder
                i +=1
            elif table[roman[i]]<table[roman[i+1]]:
                adder = table[roman[i+1]] - table[roman[i]]
                sum += adder
                i += 2
            else:
                adder = table[roman[i]]
                sum += adder
                i += 1
        return sum

test = Solution()
print(test.romanToInt('MCMXCIV'))
