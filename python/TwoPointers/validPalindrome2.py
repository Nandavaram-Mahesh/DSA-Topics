
str = "RACEACAR"

str1="madame"

def is_palindrome(s):
  
  # Replace this placeholder return statement with your code
  
  arr = list(s)

  # print(arr)
  start = 0
  end = len(arr)-1

  mismatch =0
  while start<end:
      
      if(arr[start]!=arr[end]):
        mismatch+=1
        end-=1
      else:
          start+=1
          end-=1           
  
  if mismatch>1:
    return False
  else:
    return True
  

result = is_palindrome(str)


print(result)