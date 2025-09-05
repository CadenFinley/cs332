#caden finley

def find_common_elements(list_a, list_b):
    common_elements = []
    index_a = 0
    index_b = 0

    # x = 1 .. n + m
    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] < list_b[index_b]:
            index_a += 1
        elif list_a[index_a] > list_b[index_b]:
            index_b += 1
        else:
            # list_a[index_a] == list_b[index_b]
            current_value = list_a[index_a]
            
            values_in_a = 0
            current_index_a = index_a
            while current_index_a < len(list_a) and list_a[current_index_a] == current_value:
                values_in_a += 1
                current_index_a += 1
            values_in_b = 0
            current_index_b = index_b

            while current_index_b < len(list_b) and list_b[current_index_b] == current_value:
                values_in_b += 1
                current_index_b += 1
                
            min_occurrences = min(values_in_a, values_in_b)

            for _ in range(min_occurrences):
                common_elements.append(current_value)
                
            index_a = current_index_a
            index_b = current_index_b
    
    return common_elements


if __name__ == "__main__":
    array_1 = [1, 3, 5, 7, 9]
    array_2 = [1, 2, 3, 4, 5, 6]
    print(f"A = {array_1}")
    print(f"B = {array_2}")
    print(f"Common elements: {find_common_elements(array_1, array_2)}")
    
    array_1 = [1, 2, 2, 2, 4, 4, 4, 4, 5, 5, 5]
    array_2 = [1, 1, 2, 2, 3, 4]
    print(f"A = {array_1}")
    print(f"B = {array_2}")
    print(f"Common elements: {find_common_elements(array_1, array_2)}")