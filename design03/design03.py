def make_wobbly(list):
    if len(list) < 2:
        return
    if len(list) % 2 == 0:
        print("even length, not running")
        list = []
        return
    n = len(list)
    for i in range(n - 1):
        #print(f"{i+1}: {list}")
        if i % 2 == 0: # even index
            # list[i] < list[i+1]
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                #print(f"even: {list}")
        else: # odd index
            # list[i] > list[i+1]
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                #print(f"odd: {list}")

if __name__ == "__main__":
    arr1 = [3, 1, 4, 1, 5, 9, 2]
    print("in:", arr1)
    make_wobbly(arr1)
    print("out:", arr1)

    print()

    arr2 = []
    print("in:", arr2)
    make_wobbly(arr2)
    print("out:", arr2)

    print()

    arr3 = [1]
    print("in:", arr3)
    make_wobbly(arr3)
    print("out:", arr3)

    print()

    arr4 = [2, 1]
    print("in:", arr4)
    make_wobbly(arr4)
    print("out:", arr4)

    print()

    arr5 = [1, 2, 3, 4, 5, 6]
    print("in:", arr5)
    make_wobbly(arr5)
    print("out:", arr5)

    print()

    arr6 = [6, 5, 4, 3, 2, 1]
    print("in:", arr6)
    make_wobbly(arr6)
    print("out:", arr6)
