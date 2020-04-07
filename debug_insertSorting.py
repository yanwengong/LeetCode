### debug insert sorting
### 20200105


## what is the input, for number, cannot use len(A);
## for string, it's immutable => note, input is array..
def insertSort(A):
    if len(A) <= 1:
        return A

    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while j >= 0  and A[j] > k:
            A[j + 1] = A[j]
            A[j] = k # added
            j -= 1


    return A
B = [3,2,1,2]
result = insertSort(B)
print(result) #[3,3,3,3]

C = [1,3,2]
result = insertSort(C)
print(result) #correct

D = [1,2,3,0]
result = insertSort(D)
print(result) #correct

def insertSort0(A):
    if len(A) <= 1:
        return A

    for i in range(1, len(A)):
        k = A[i]
        j = i - 1
        while j >= 0  and A[j] > k:
            A[j + 1] = A[j]
            #A[j] = k # added
            j -= 1

        A[j + 1] = k


    return A
