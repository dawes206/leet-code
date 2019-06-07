# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        if not nums:
            return []
        for i in range(len(nums)):
            # print(i)
            if i == len(nums)-1:
                val = nums[i]
                while len(nums) - val >= 0:
                    val += 1
                    missing.append(val)
                return missing
            if nums[i+1]-nums[i] == 1 or nums[i+1]-nums[i] == 0:
                continue
            else:
                val = nums[i]
                while nums[i+1] - val != 1:
                    val += 1
                    missing.append(val)
                continue
