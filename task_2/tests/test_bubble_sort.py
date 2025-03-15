from ..bubble_sort import bubble_sort

def test_bubble_sort():
    # Test 1: Basic test
    assert bubble_sort([2, 1, 5, 4, 7]) == [1, 2, 4, 5, 7]

    # Test 2: List with negative numbers and duplicates
    assert bubble_sort([2, -5, -3, 3, 1, 2]) == [-5, -3, 1, 2, 2, 3]

    # Test 3: Empty list
    assert bubble_sort([]) == []

    # Test 4: List with a single element
    assert bubble_sort([1]) == [1]

    # Test 5: Additional test
    assert bubble_sort([5, 3, 8, 1, 2]) == [1, 2, 3, 5, 8]

    print("All tests passed!")

if __name__ == "__main__":
    test_bubble_sort()