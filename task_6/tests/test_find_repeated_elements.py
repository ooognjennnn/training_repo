from task_6.find_repeated_elements import find_repeated_elements

def test_find_repeated_elements():
    # Test 1: List with repeats
    result = find_repeated_elements([4, 3, 3, 1, 1, 2])
    assert sorted(result) == [1, 3], f"Expected [1, 3], got {result}"

    # Test 2: No repeats
    result = find_repeated_elements([1, 2, 3, 4])
    assert result == [], f"Expected [], got {result}"

    # Test 3: All repeats
    result = find_repeated_elements([1, 1, 1, 1])
    assert result == [1], f"Expected [1], got {result}"

    # Test 4: Empty list
    result = find_repeated_elements([])
    assert result == [], f"Expected [], got {result}"
