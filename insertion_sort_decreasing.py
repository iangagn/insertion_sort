def insertion_sort_decreasing(arr):
  '''
  Implementation of insertion sort.

  Sorts in decreasing order.

  Parameters
  ----------
  arr : list, tuple or set
      An array.
      
  Returns nothing.
  '''

  for i in range(1, len(arr)):
    j = i
    while arr[j] > arr[j - 1] and j > 0:
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      j -= 1
