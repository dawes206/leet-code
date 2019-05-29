#given staircase of n steps, how many distinct ways can you climb to the top given that you can take steps 1 or 2 at at ime

# input: 2
# output: 2
# [1+1, 2]


#brute force
# ans = []
# x = [1]*3
# for i in range(3):
#     if sum(x) = 3:
#
# def solution(n):
#     ans = []
#     for i in range(n):
#         x = [1]*n
#         ans.append(x)
#     for i in range(n-1):
#         x=[1]*(n-1)
#         x[i] = 2
#         ans.append(x)

# def solution(n):
#     ans = []
#     counter = 0
#     while n-counter != 0:
#         for i in range(n-counter):
#             x=[1]*(n-counter)
#             x[i] = 2
#             if sum(x) == n:
#                 ans.append(x)
#         counter +=1
#     return(ans)
#
# print(solution(3))


class Solution:
    def climb_stairs(curr_step, n):
        if curr_step > n:
            return 0
        if curr_step == n:
            return 1
        return climb_stairs(curr_step+1, n) + climb_stairs(curr_step+2, n)


test = Solution()
print(test.climb_stairs(0,5))
