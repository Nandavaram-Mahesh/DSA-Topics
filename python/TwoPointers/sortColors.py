
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