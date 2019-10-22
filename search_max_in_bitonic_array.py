# Bitonic array: values first increase, reach a peak or max and then decrease

def find_max_in_bitonic_array(arr):
  # TODO: Write your code here
  if arr is None:
    return None
  start, end = 0, len(arr)-1
  while start < end :
    mid = (start+end)//2
    if arr[mid+1] > arr[mid]:
      # we are in left half, move right
      start = mid+1
    elif arr[mid+1] < arr[mid]:
      # we are in right half were
      # values decrease from left to right 
      # so move left
      end = mid # because mid could be index of max element
  return arr[start]

  


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()
