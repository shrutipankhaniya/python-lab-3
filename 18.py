def selectionsort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[idx], input_list[min_idx] = input_list[min_idx],input_list[idx]
l = [22,13,4,8,17,26,53,4]
selectionsort(l)
print(l)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

elements = [22, 13, 4, 8, 17, 26, 53, 4]
selection_sort(elements)
print("Sorted elements:", elements)
