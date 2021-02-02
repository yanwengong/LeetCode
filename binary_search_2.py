## second attempt on binary search
## given sorted array and a number, return the index of the number
## based on this template: https://erinz.gitbooks.io/jiuzhang-basic-algorithms/chapter-2---binary-search.html


def binary_search2(array, num):

    start = 0
    end = len(array) - 1

    while start +1 < end:
        mid = int((start + end)/2)
        if array[mid] == num:
            return mid
        elif array[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

    if array[start] == num:
        return start
    elif array[end] == num:
        return end
    else:
        print("number not in array")
        return None

input = [1,2,3,4,5,6,7]
x = binary_search2(input, 7)
print(x)



######## wrong answer below ####################
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid_index = int(len(nums)/2)
        max_index = int(len(nums) - 1)
        min_index = 0

        if len(nums) == 1 and nums[0] == target: return 0

        while mid_index >= 0 and mid_index!= max_index and mid_index!= min_index:
            if nums[mid_index] < target:
                min_index = mid_index
                mid_index = int((mid_index + max_index)/2)
            elif nums[mid_index] > target:
                max_index = mid_index
                mid_index = int((mid_index-min_sindex)/2)
            elif nums[mid_index] == target:
                return mid_index
        # issue: index back and forth

        return -1
