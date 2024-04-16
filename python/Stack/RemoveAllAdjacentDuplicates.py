from collections import deque

def remove_duplicates(string):
    stack = deque()
    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)


inputs = ["g", 
        "ggaabcdeb", 
        "abbddaccaaabcd",
        "aannkwwwkkkwna", 
        "abbabccblkklu"
    ]
for i in inputs:
    
    result = remove_duplicates(i)
    print(result) 


