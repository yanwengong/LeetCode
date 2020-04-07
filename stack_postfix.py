
## solve the postfix question by using list as stack
## https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/


def profix(input_array):
    result_stack = []
    for i in range(len(input_array)):
        while True:
            try:
                val = int(input_array[i])
                result_stack.append(val)
                break
            except ValueError: #means it is not int but operator
                num2 = result_stack.pop()
                num1 = result_stack.pop()
                new_val = str(eval(str(num1) + input_array[i] + str(num2)))
                result_stack.append(new_val)
                break
    return(result_stack)

print(profix(["2", "3", "1", "*", "+", "9", "-"]))
