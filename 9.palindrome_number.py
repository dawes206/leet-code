#determine whether a number is a palindrome.
#
# input: 10
# output: false
#
# input: 121
# output: true

class Solution:
    def isPalindrome(self, x: int):

        num_list = list(str(x))
        num_rev = num_list[::-1]
        if num_list == num_rev:
            return True
        else:
            return False



testCase1 = -121

test = Solution()
print(test.isPalendrome(testCase1))
