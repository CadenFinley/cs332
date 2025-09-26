
# caden finley
def localMaximum(a, n):
    
    # T(n) = T(n/2) + O(1)
    # runtime O(log n)
    
    left = 1
    right = n
    
    while left <= right:
        if left == right:
            return left
        
        if right - left == 1:
            if a[left] > a[right]:
                return left
            else:
                return right
        
        # (n/2)
        mid = (left + right) // 2
        is_local_max = True

        if mid > 1 and a[mid] <= a[mid - 1]:
            is_local_max = False
        
        if mid < n and a[mid] <= a[mid + 1]:
            is_local_max = False
        
        if is_local_max:
            return mid
        
        # set larger neighbor side
        if mid > 1 and a[mid - 1] > a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    # this will not be reached
    return left

def main():
    file = open('local-maximum-test.txt', 'r')
    k = int(file.readline().strip()) # first line is number of test cases
    print(f"number of test cases: {k}")
    for j in range(k):
        line = file.readline().strip()
        print(f"input  {j + 1}: {line}")
        values = list(map(int, line.split()))
        n = values[0]  # first value is number of test values
        test_values = values[1:n+1]
        '''
        In this localMaximum function, you MUST have the test data populating indices [1..n] and your
        solution must treat [1..n] as the valid range of values. Any solution that puts test data into index
        0 or accesses that for any reason in the localMaximum function will be scored ZERO
        
        A[1..n]
        A[   |   |   |   |   |   |   |   ]
           1   2   3   4   5   6   7   8
        
        '''
        a = [0] + test_values  # a[0] is unused a[1..n]
        result = localMaximum(a, n)
        print(f"output {j + 1}: index: {result} value: {a[result]}")

if __name__ == "__main__":
    main()
