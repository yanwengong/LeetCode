## https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
## give a array of number and operator, calculate the final result
## acutaully, this is not correct..


def sep(input_array):
    op_set = set(["+", "-", "*", "/"])
    op =[]
    num = []
    for i in range(len(input_array)):
        if input_array[i] in op_set:
            op.append(input_array[i])
        else:
            num.append(int(input_array[i]))
    return(num, op)

def cal(num, op):
    val = num[0]
    for i in range(1,len(num)):
        if op[i-1] == "+":
            val += num[i]
        elif op[i-1] == "-":
            val -= num[i]
        elif op[i-1] == "*":
            val *= num[i]
        else:
            val /= num[i]
    return val

def main(input_array):
    num, op = sep(input_array)
    ## check length
    if len(num) != len(op) + 1:
        print("The length is not correct.")
        return

    return(cal(num, op))

print(main(["1", "3", "4", "5", "+", "*","-"]))
