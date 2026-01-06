def bins(arr, key):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == key:
      return mid

    if arr[mid] < key:
      left = mid + 1
    else:
      right = mid - 1

  return -1

def steps(arr, key):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    yield left,mid,right

    if arr[mid] == key:
      return

    if arr[mid] < key:
      left = mid + 1
    else:
      right = mid - 1

  return -1
