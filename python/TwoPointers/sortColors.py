
# 0-red
# 1-white
# 2 - blue



# BRUTE FORCE APPROACH

# Time Complexity- O(n^2)
# Space Complexity - O(n)
arr=[2,2,0,1,2,2,0,2]
new_list = []

for i in range(3):
    for j in arr:
        if j==i:
            new_list.append(i)

print(new_list)



# Approach-2 
# Time Complexity - O(nlogn)

# arr.sort()


# Approach -3 

# Time Complexity - O(N)

colors = [2,2,0,1,2,2,0,2]
start=0
current=0
end = len(colors)-1    

while current<=end:
    if colors[current] == 0:
        if colors[start] != 0:
            colors[start], colors[current] = colors[current], colors[start]
            
        current += 1
        start += 1

    elif colors[current] == 1:
        current += 1

    else:
        if colors[end] != 2:
            colors[current], colors[end] = colors[end], colors[current]

        end -= 1

print(colors)