from collections import deque
def isValidParenthesis(string):

    open_parenthesis = ["(","{","["]

    hash_map={
        "{":"}",
        "[":"]",
        "(":")"
    }
    stack = deque()
    for i in range(len(string)):
        if (i==len(string)-1) and len(stack)==0 and (string[i]=="]" or string[i]=="}" or string[i]==")"):
            return False
        else:
            if  stack and hash_map[stack[-1]]==string[i]:
                stack.pop()
            
            elif string[i] in open_parenthesis:
                stack.append(string[i])

    lenght_of_stack = len(stack)
    
    return lenght_of_stack





str1 = ")))[{{}}{"
stack_length =isValidParenthesis(str1)

if stack_length==0:
    print(True)
else:
    print(False)

