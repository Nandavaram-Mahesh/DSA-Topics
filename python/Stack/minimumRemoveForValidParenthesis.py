from collections import deque
def min_remove_parentheses(s):
    
    # Replace this placeholder return statement with your code
    stack = deque()
    s_list = list(s)
    for index,value in enumerate(s):
        
        # Bad Logic

        # if not stack and value =="(" or value==")":
        #     stack.append([value,index])
        # elif (stack and stack[-1][0]=="(" and value==")"):
        #     stack.pop()
        
        # right logic
        if (stack and stack[-1][0]=="(" and value==")"):
            stack.pop()
        elif value=='(' or value==")":
            stack.append([value,index])

    # return stack

    for i in stack:
        s_list[i[1]]=""
    
    return "".join(s_list)

result = min_remove_parentheses("ab)ca(so)(sc(s)(")
print(result)