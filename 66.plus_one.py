# input: [1,2,3]
# output: [1,2,4]
import os
import psutil

#Uses 13.2 MB, which is better than 30% of users. However, it used to take up 13.6, and was only better than 5%... Other times it's 80%. So, I'm guessing that the test case differs.
# class Solution():
#     def plusOne(self,nums):
#         for i in range(1, len(nums)+1):
#             print(i)
#             if nums[-i]+1 != 10:
#                 nums[-i] += 1
#                 return nums
#             elif i == len(nums):
#                 nums[-i] = 0
#                 return [1] + nums
#             else:
#                 nums[-i] = 0
#         return nums
#

#Below uses around 13.1MB, which I guess is noticeably less than the other one. THis solution beats out 77.17% of other users
class Solution2():
    def plusOne(self,nums):
        mapped = map(lambda x: str(x), nums)
        num = ''.join(mapped)
        num = int(num)+1
        num_list = list(str(num))
        num_list_mapped = map(lambda x: int(x), num_list)
        return list(num_list_mapped)

test = Solution2()
print(test.plusOne([9,9,9,9,9,9,9,9,9]))
process = psutil.Process(os.getpid())
print(process.memory_info().rss)


# if last number == 10
#     set it equal to zero
#     move to next value
#     check if it's == 10
#     if so, move to next
#     if not, just subtract 1
# else just add 1
#
#
# for every number, starting from back
#     if number + 1 != 10
#         number + 1
#         return
#     else
#         set number = 0
#         move to next number
#         if number +1 !=10
#             number + 1
#             return
#         else
#             set number = 0
#             move to next number...
