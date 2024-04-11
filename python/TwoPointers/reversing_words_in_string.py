
# Total Time Complexity - O(4N) -> O(N)

str = "We love Python "

str2 = "1234 abc XYZ"

str3 = "You are amazing"

str4 = "Hello     World"

str5 = "Greeting123"
# O(N)
splittedStr = str5.split(" ") 

start = 0
end= len(splittedStr)-1

# O(N)
while start<end:
    if splittedStr[start]=="" and splittedStr[end]!="":
        start+=1
    elif splittedStr[end]=="" and splittedStr[start]!="":
        end-=1
    elif(splittedStr[end]=="" and splittedStr[start]==""):
        start+=1
        end-=1
    elif(splittedStr[start]!="" and splittedStr[end]!=""):
        splittedStr[start],splittedStr[end] =splittedStr[end],splittedStr[start]
        start+=1
        end-=1
        
     
    
# print(splittedStr)
print("SPACES MULTIPLE")

# O(N)
sortedArray = (' ').join(splittedStr)

# O(N)
strippedSortedArr = sortedArray.strip(" ")

print(strippedSortedArr)