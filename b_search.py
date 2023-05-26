def binary_search(arr,target):
  low=0
  high=len(arr)-1
  
  while low<=high:
    mid=(low+high)
    guess=arr[mid]
    
    if guess == target:
      return mid
    elif guess < target:
      low=mid+1
      else:
        high=nid-1
        return -1
      
numbers=[2,5,34,6,4,7,3,88,10,1]
target_number=5

result=binary_search(numbers,target_number)
if result i=-1;
print("Target Found at index",result)

else:
  print("Target not found")
