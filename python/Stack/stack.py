from collections import deque

# deque  - Doubly Ended Que

# Find if the given string is valid , valid Condition  - should have opening and closing brackets and the stack should be empty finally. 

def isValidBracketString(str):
    
    # To check if the given string has a closed Bracket
    bracketMapping = {"{":"}","[":"]","(":")"}

    # To check if the given string has open Brackets 
    openBrackets = ["{","[","("]
    
    # assigning deque to the stack variable 
    stack = deque()

    for s in str:
        # Checking for open brackets
        if s in openBrackets:
            stack.append(s)
        # if the string is not open bracket ,  check if we have item in the stack and check if matches bracketMapping ,
        #  if it matches pop element from stack  
        # bracketMapping[stack[-1]] - top most element in the stack  
        elif stack and s == bracketMapping[stack[-1]]:
            stack.pop()
        else:
            return False
    # Finally after looping through the entire string then we are checking if the stack is empty, 
    # if it is empty then it is a valid Bracket string. 
    return stack == deque()


# Driver Code
bracketstr = "([])"
isValidBracketStr = isValidBracketString(bracketstr)

if(isValidBracketStr):
    print("The given string is valid")
else:
    print("The given string is not valid")
    

