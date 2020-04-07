## count primes
## given larger integer N, return the number of primes in range [1,2,...,N]

def check_prime(input):
    if input > 1:
        for i in range(2, input):
            if (input % i) == 0:
                return False
        print(input)
        return True
    else:
        return False

def count_prime(intN):
    count = 0
    if intN > 1:
        for i in range(2, intN+1):
            if check_prime(i):
                count += 1
    return count

print(count_prime(30))
