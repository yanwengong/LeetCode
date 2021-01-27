## subarray sum equals K
## https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if sum(nums[i: j]) == k:
                    counter += 1

        return counter


#         length = len(nums)

#         counter = 0
#         ## two pointer
#         i = 0

#         sum_val = nums[i]

#         while i < length :
#             if nums[i] == k:
#                 counter += 1
#                 j = i+1
#                 while j < length:
#                     if nums[j] == 0:
#                         counter += 1
#                     j += 1

#             #elif nums[i] < k:
#             else:
#                 j = i + 1
#                 sum_val = nums[i]
#                 while j < length :
#                     sum_val += nums[j]
#                     if sum_val == k:
#                         counter += 1
#                     j += 1
#             i += 1

#         return counter
