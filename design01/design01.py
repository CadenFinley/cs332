#caden finley
#array = [ -1, 3, -2, 7, -9, 0, 7 ]

def sum_in_range(arr, start, end):
    total = 0
    for k in range(start, end + 1):
        total += arr[k]
    return total


def maximum_subsequence_sum(arr):
    largest_sum = 0
    current_largest = []

    #base cases
    #all inputs are positive
    if all(x > 0 for x in arr):
        current_sum = sum_in_range(arr, 0, len(arr) - 1)
        print("The largest sum is: ", current_sum)
        print("The subarray with the largest sum is: ", arr)
        return

    #all inputs are negative or empty
    if all(x < 0 for x in arr) or len(arr) == 0:
        print("The largest sum is: 0")
        print("The subarray with the largest sum is: []")
        return
    
    for i in range(len(array)):
      for j in range(len(array)-1, i, -1):
        #so now i have pointer at start and end of sub array
        #now i just need to add all number of the sub array
        current_sum = sum_in_range(array, i, j)
        if current_sum > largest_sum:
            largest_sum = current_sum
            current_largest = array[i:j+1]

    print("The largest sum is: ", largest_sum)
    print("The subarray with the largest sum is: ", current_largest)

if __name__ == "__main__":
  print("please enter a list of integers separated by commas:")
  user_input = input()
  #empty input
  if user_input.strip() == "":
      array = []
  else:
      array = list(map(int, user_input.split(",")))
  maximum_subsequence_sum(array)
