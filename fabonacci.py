## Natera code interview
## https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/


## original (for loop, space optimize)

def fib(n):
    pre = 0
    curr = 1

    for i in range(n):
        next = pre + curr
        pre = curr
        curr = next

    return curr

print(fib(5))


## recursion

def fib_recur(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 1

    elif n == 1:
        return 1

    else: return fib_recur(n-2) + fib_recur(n-1)

print(fib_recur(5))

## dynamic programming
## TODO: understand dynamic programming
fibArray = [0, 1]

def fib_dynamic(n):

    if n < 0:
        print("Incorrect input")

    elif n < len(fibArray):
        return fibArray[n]

    else:
        temp_fib = fib_dynamic(n-2) + fib_dynamic(n-1)
        fibArray.append(temp_fib)
        return temp_fib

print(fib_dynamic(5))
