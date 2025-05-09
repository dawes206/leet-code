# input: [1,2,3]
# output: [1,2,4]
import os
import psutil


class Solution():
    def plusOne(self,nums):
        for i in range(1, len(nums)+1):
            print(i)
            if nums[-i]+1 != 10:
                nums[-i] += 1
                return nums
            elif i == len(nums):
                nums[-i] = 0
                return [1] + nums
            else:
                nums[-i] = 0
        return nums

test = Solution()
print(test.plusOne([9,9,9]))
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
