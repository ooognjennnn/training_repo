def bubble_sort(array: list) -> list:
    n = len(array)
    for i in range(n):
        # Going through the array
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Swapping the elements
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


