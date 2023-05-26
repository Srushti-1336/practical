def binary_search(arr,target):
  low=0
  high=len(arr)-1
  
  while low <=high:
    mid = (low+high)
    guess=arr[mid]
     
      
      if guess == target:
        return mid
      elif guess< target:
        low = mid+1
        else:
          high=mid-1
   return -1 #target not found
      
      
numbers=[2,3,8,4,5,9.7,1]
target_number=5
      
result = binary_search(numbers,target_number)
      
if result i=-1:
  print("target found at index",result)
  else:
    print("target not found")
