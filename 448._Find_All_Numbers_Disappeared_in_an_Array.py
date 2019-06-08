class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    new = [0]*(len(nums)+1)
    results = []
    for i in nums:
        new[i] = i
    for i in range(len(new)):
        if new[i] == 0:
            results.append(i)
    return results[1:]
