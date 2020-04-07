## count prime
## Sieve of Eratosthenes
import math as m
def count_prome_SE(input_num):

    if input_num == 2:
        return 0
    ## init matrix as all True
    prime_matrix = [True]*(input_num-1)
    for i in range(2, input_num + 1): #i is number
        if prime_matrix[i-2]: #i - 2 is index
            for j in range(2, int(input_num/i) + 1): # here j is number
                # print(i*j)
                prime_matrix[i*j - 2] = False # i*j -2 is index

    for i in range(2, input_num + 1):
        if prime_matrix[i-2]:
            print(i)

    return sum(prime_matrix)

print(count_prome_SE(100000))
