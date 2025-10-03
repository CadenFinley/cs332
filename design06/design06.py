from __future__ import annotations
import sys

# caden finley

def search(k, matrix, n):

    if n == 0:
        return False

    row = 0
    col = n - 1
    #runs = 0

    # O(n)
    while row < n and col >= 0:
        #runs += 1
        current = matrix[row][col]
        if current == k:
            #print(f"runs: {runs}")
            return True
        if current > k:
            col -= 1
        else:
            row += 1

    #print(f"runs: {runs}")
    return False


'''
[
    4
    1 2 3 4
    2 3 4 5
    3 4 5 6
    4 5 6 7
    3 6 9
]

'''


def read_file(path):
    with open(path, "r", encoding="utf-8") as infile:
        raw_lines = [line.strip() for line in infile if line.strip()]

    n = int(raw_lines[0])

    matrix_rows = raw_lines[1 : n + 1]
    matrix = []
    for line in matrix_rows:
        row_values = list(map(int, line.split()))
        matrix.append(row_values)

    search_values = []
    for line in raw_lines[n + 1 :]:
        search_values.extend(map(int, line.split()))

    return n, matrix, search_values


def main():
    n, matrix, search_values = read_file(sys.argv[1])

    for value in search_values:
        found = search(value, matrix, n)
        status = "found" if found else "not found"
        print(f"{status} {value}")


if __name__ == "__main__":
    main()

