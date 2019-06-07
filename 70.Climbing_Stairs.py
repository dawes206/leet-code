# # You are climbing a stair case. It takes n steps to reach to the top.
# #
# # Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# #
# # Note: Given n will be a positive integer.
# #
# # Example 1:
# #
# # Input: 2
# # Output: 2
# # Explanation: There are two ways to climb to the top.
# # 1. 1 step + 1 step
# # 2. 2 steps
# # Example 2:
# #
# # Input: 3
# # Output: 3
# # Explanation: There are three ways to climb to the top.
# # 1. 1 step + 1 step + 1 step
# # 2. 1 step + 2 steps
# # 3. 2 steps + 1 step
#
#
# # n = 5
#     #                    0
#     #               /         \
#     #             1             2
#     #           /    \         /  \
#     #         2         3      3    4
#     #        /  \      / \    / \  /
#     #      3     4    4   5  4   5 5
#     #     / \   / \  / \    /
#     #   4    5 5   6 5  6  5
#     #  /
#     # 5
#
#
# #Each leaf represents a unique permutation. I think that means that we just have to count all the leaves that are == 5
# #if we're at step 0, we want to know what step we're on after 1 step and after 2 step
# #on step 1, we want to know what step we're on after 1 step and after 2 step, AND if on step 2 we want to know after 1 step and 2 step
#
class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0]
        solved_steps = {}
        sum = self.helper(0,n, count, solved_steps)
        # return count[0]
        return sum

    def helper(self,currentStep,finalStep, count, solved_steps):
        if currentStep == finalStep:
            count[0] += 1
            # print('step 5')
            return 1
        elif currentStep > finalStep:
            # print('step 6')
            return 0
        elif currentStep in solved_steps:
            # print('Step {} in dict'.format(currentStep))
            # print(solved_steps)
            return solved_steps[currentStep]
        else:
            num1 = self.helper(currentStep+1, finalStep, count, solved_steps)
            # print('num1: ', num1)
            num2 = self.helper(currentStep+2, finalStep, count, solved_steps)
            # print('num2: ', num2)
            sum = num1+num2
            # print('sum worked: ', sum)
            solved_steps[currentStep] = sum
            return sum

test = Solution()
print(test.climbStairs(34))
