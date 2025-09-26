
# caden finley
def find_local_maximum(a, left, right):
  
  # T(n) = T(n/2) + O(1)
  # runtime O(log n)
    
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
    
    n = len(a) - 1
    if mid < n and a[mid] <= a[mid + 1]:
        is_local_max = False
    
    if is_local_max:
        return mid
    
    # 1T(n/2)
    if mid > 1 and a[mid - 1] > a[mid]:
        return find_local_maximum(a, left, mid - 1)
    else:
        return find_local_maximum(a, mid + 1, right)

def main():
    file = open('local-maximum-test.txt', 'r')
    length = int(file.readline().strip())
    for _ in range(length):
        line = file.readline().strip()
        print(f"input: {line}")
        values = list(map(int, line.split()))
        '''
        In this localMaximum function, you MUST have the test data populating indices [1..n] and your
        solution must treat [1..n] as the valid range of values. Any solution that puts test data into index
        0 or accesses that for any reason in the localMaximum function will be scored ZERO
        
        A[1..n]
        A[   |   |   |   |   |   |   |   ]
           1   2   3   4   5   6   7   8
        
        '''
        length = len(values)
        a = [0] + values  # a[0] is unused a[1..n]
        result = find_local_maximum(a, 1, length)
        print(f"output: index: {result} value: {a[result]}")

if __name__ == "__main__":
    main()
