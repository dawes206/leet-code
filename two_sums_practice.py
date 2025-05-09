import time
class Solution:
    # def twoSum(self, nums: list, target: int):
    #     for i in nums:
    #         for x in nums:
    #             if i+x == target:
    #                 return [nums.index(i), nums.index(x)]

    def twoSum2(self, nums: list, target: int):
        for i in nums:
            if target-i in nums[nums.index(i)+1:]:
                if target-i == i:
                    return [nums.index(i), len(nums)-(nums[::-1].index(i)+1)]
                else:
                    return [nums.index(i), nums.index(target-i)]
    # def twoSum3(self, nums: list, target: int):
    #     x = []
    #     for i in nums:
    #         x.append(i)
    #         if target - i !=i and target-i in nums:
    #             if target-i in x:
    #                 return [nums.index(i), x.index(target-i)]
    #             else:
    #                 return [nums.index(i), nums.index(target-i)]

# def create_dataset(size):
#     dataset = list(range(1,size))
#     for i in dataset[1:int(size/2)-2]:
#         dataset.remove(size-i)
#     return dataset



# test = Solution()
# greeting = test.twoSum([1,2],2)
#
# dataset = create_dataset(10000)
#

answer = Solution()
# time1 = time.perf_counter()
# print(answer.twoSum(dataset,10000))
# time2 = time.perf_counter()
print(answer.twoSum2([2,7,11,15],9))
# time3 = time.perf_counter()
# print(answer.twoSum3(dataset,10000))
# time4 = time.process_time()
#[1, 2, 7, 8, 11, 15],15)

# print('time for first', time2-time1)
# print('time for 2nd', time3-time2)
# print('time for 3rd', time4-time3)
