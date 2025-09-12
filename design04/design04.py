# caden finley
def find_sum_pair_100(A, B):
    target = 100
    if not A or not B:
        return None # no pairs possible
    
    i = 0 # start from smallest in A
    j = len(B) - 1 # start from largest in B
    
    # O(n) runtime
    while i < len(A) and j >= 0:
        current_sum = A[i] + B[j]
        
        if current_sum == target:
            return (A[i], B[j])
        elif current_sum < target:
            i += 1  # need larger sum so move A pointer right
        else:
            j -= 1  # need smaller sum so move B pointer left

    return None

A1 = [2, 2, 3, 5, 7, 7, 7, 8, 11, 13]
B1 = [-10, -5, 0, 0, 2, 5, 8, 12, 12, 12, 15]

A2 = [1, 5, 10, 15, 20]
B2 = [80, 85, 90, 95, 99]

A3 = [50]
B3 = [50]

A4 = [10, 20, 30, 40, 50]
B4 = [90, 80, 70, 60, 50]

A5 = [1, 2, 3, 4, 5]
B5 = [101, 102, 103, 104, 105]

A6 = [90, 95, 99]
B6 = [1, 5, 10]

A7 = []
B7 = [1, 2, 3, 4, 5]

A8 = [1, 2, 3]
B8 = []

A9 = [-50, -25, 0, 25, 50, 75]
B9 = [25, 50, 75, 100, 125, 150]

A10 = [100]
B10 = [0]

if __name__ == "__main__":
    print(find_sum_pair_100(A1, B1))
    print(find_sum_pair_100(A2, B2))
    print(find_sum_pair_100(A3, B3))
    print(find_sum_pair_100(A4, B4))
    print(find_sum_pair_100(A5, B5))
    print(find_sum_pair_100(A6, B6))
    print(find_sum_pair_100(A7, B7))
    print(find_sum_pair_100(A8, B8))
    print(find_sum_pair_100(A9, B9))
    print(find_sum_pair_100(A10, B10))