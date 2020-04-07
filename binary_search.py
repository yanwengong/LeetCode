## binary search
## given sorted array and a number, return the index of the number



def binary_search(input_array, left, right, number):
    if left > right:
        return -1
    #elif left > len(input_array):
    #    return -1
    else:
        mid_ind = int((right + left)/2)
        print(mid_ind)
        if input_array[mid_ind] == number:
            return mid_ind
        elif input_array[mid_ind] > number:
            return(binary_search(input_array, left, mid_ind-1, number))
        elif input_array[mid_ind] < number:
            return(binary_search(input_array, mid_ind+1, right, number))

input = [1,2,3]
#print(binary_search(input, 0, len(input), 0))


def binary_search(input_array, left, right, number):
    if left == right:
        return -1
    #elif left > len(input_array):
    #    return -1
    else:
        mid_ind = int((right + left -1)/2)
        print(mid_ind)
        if input_array[mid_ind] == number:
            return mid_ind
        elif input_array[mid_ind] > number:
            return(binary_search(input_array, left, mid_ind, number))
        elif input_array[mid_ind] < number:
            return(binary_search(input_array, mid_ind+1, right, number))

print(binary_search(input, 0, len(input), 4))
