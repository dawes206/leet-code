#given 32 bit signed integer, reverse digits
# input: 123
# oiutput: 321
#
# input: -123
# output: -321
#
# input: 120
# output: 21

class Solution():

    def string_manip(self, num):
        is_neg=False
        if num < 0:
            is_neg = True
            num = abs(num)
        num_string = str(num)
        reversed_list = list(str(num))[::-1]
        reversed_num = ''.join(reversed_list)
        if int(reversed_num) > 2**31:
            return 0
        if is_neg == True:
            return 0 - int(reversed_num)
        else:
            return int(reversed_num)

test = Solution()
print(test.string_manip(1534236469))

# class Solution():
#     def int_manip(self,num):
#         is_neg = False
#         if num <0:
#             is_neg = True
#             num=abs(num)
#         while i < num left:
#             num%10 *10
#
#
# for i in length number:
#     new number = lentgh(number)*10*num%i + itself
#
# for i in [1,2,2]:
#     new number = new number + i * 10*(position-1)
#
# for i in range(length(num)):
#     new number= new number + num%
