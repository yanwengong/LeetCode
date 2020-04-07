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
