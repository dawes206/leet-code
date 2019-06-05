# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

#for val in input, find max of
# Have a empty value most
# instead of going through every number, you can eliminate numbers who's value * remaining poosition in graph < most

# for each val in input, only need to look at other values that are equal to or larger than itself (each iteration gets shorter)
# for each val in input, find the max value of

# class Solution:
#     def maxArea(self, height):
#         max = 0
#         for j in range(len(height)):
#             for i in range(len(height)):
#                 if height[i] >= height[j] and height[j]*(abs(i-j))>max:
#                     # print('i: ', i)
#                     # print('j: ',j)
#                     # print('height: ', height[j])
#                     max = height[j]*(abs(i-j))
#                     # print('max: ', max)
#                     # print('\n')
#         return max

class Solution:
    def maxArea(self, height):
        l, r = 0, len(height)-1
        max = 0
        while l != r:
            area = min(height[l],height[r])*(r-l)
            if area>max:
                max = area
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return max




test = Solution()
height = [2,3,4,5,18,17,6]
print(test.maxArea(height))
