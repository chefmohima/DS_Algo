def search_rotated_array(arr, key):
  start, end = 0, len(arr) - 1
  last = arr[-1]
  while start <= end:
      mid = (start+end)//2
      if arr[mid] == key:
          return mid
      # first determine which half of the array are you in
      # then compare key to arr[mid]
      if arr[mid] > last:
          # in first half, decreases to left
          if arr[mid] > key:
              end = mid-1
          else:
              start = mid+1
      elif arr[mid] <= last:
          # in second half, increases to right
          if arr[mid] > key:
              start = mid+1
          else:
              end = mid-1
  return mid
              
      
              
    
    



def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()
