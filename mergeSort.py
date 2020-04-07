
def merge(inputArray1, inputArray2):


    new_array = inputArray1 + inputArray2
    #print(new_array)
    i = j = k =0
    while i < len(inputArray1) and j < len(inputArray2):
        if inputArray1[i] < inputArray2[j]:
            new_array[k] = inputArray1[i]
            i += 1
        else:
            new_array[k] = inputArray2[j]
            j += 1
        k += 1
    if i == len(inputArray1):
        new_array[k:] = inputArray2[j:]
    else:
        new_array[k:] = inputArray1[i:]

    return new_array

A = merge([2,4,5], [1,3,3])  ## note: need to give exactly 2 input
print(A)
def mergeSort(inputArray):
    #print(inputArray)
    mid_index = int(len(inputArray)/2)

    if mid_index == 0:
        output = inputArray

    else:
        L = inputArray[0:mid_index]
        R = inputArray[mid_index:]


        new_L = mergeSort(L)
        #print(new_L)
        new_R = mergeSort(R)
        #print(new_R)
        output = merge(new_L, new_R)

    return output
inputArray3 = [1,4,2,3]
print(mergeSort(inputArray3))
