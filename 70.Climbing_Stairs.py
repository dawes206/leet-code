# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# n = 5
    #                    0
    #               /         \
    #             1             2
    #           /    \         /  \
    #         2         3      3    4
    #        /  \      / \    / \  /
    #      3     4    4   5  4   5 5
    #     / \   / \  / \    /
    #   4    5 5   6 5  6  5
    #  /
    # 5


#Each leaf represents a unique permutation. I think that means that we just have to count all the leaves that are == 5
#if we're at step 0, we want to know what step we're on after 1 step and after 2 step
#on step 1, we want to know what step we're on after 1 step and after 2 step, AND if on step 2 we want to know after 1 step and 2 step

class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0]
        self.helper(0,n, count)
        return count[0]

    def helper(self,currentStep,finalStep, count):
        if currentStep == finalStep:
            count[0] += 1
            return
        elif currentStep > finalStep:
            return
        else:
            self.helper(currentStep+1, finalStep, count)
            self.helper(currentStep+2, finalStep, count)

test = Solution()
print(test.climbStairs(34))

class Solution
