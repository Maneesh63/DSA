from pickletools import read_stringnl


def valid_parenthesis(arr):

    stack_dict ={"[": "]", "{": "}", "(": ")"}
    stack = []
    for i in arr:
        if i in stack_dict:
            stack.append(i)

        elif i not in stack_dict:
             if stack_dict[stack.pop()] != i:
                 return False


    print("valid parenthesis", stack)
    return len(stack) == 0

print(valid_parenthesis("()[]{}"))






