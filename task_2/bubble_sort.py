def bubble_sort(array: list) -> list:
    n = len(array)
    for i in range(n):
        # Prolazimo kroz listu i upoređujemo susedne elemente
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Menjamo mesta ako su elementi u pogrešnom redosledu
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    # Testovi
    assert bubble_sort([2, 1, 5, 4, 7]) == [1, 2, 4, 5, 7]
    assert bubble_sort([2, -5, -3, 3, 1, 2]) == [-5, -3, 1, 2, 2, 3]
    assert bubble_sort([]) == []  # Empty list
    assert bubble_sort([1]) == [1]  # List with one element
    assert bubble_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]
    print("All tests passed!")