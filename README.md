# Repeated Elements Task

This task implements a function to find all repeated elements in a list of integers.

## Overview
The `find_repeated_elements` function takes a list of integers and returns a list of elements that appear more than once.

## Files
- **`task_6/find_repeated_elements.py`**: Contains the function to find repeated elements.
- **`task_6/tests/test_find_repeated_elements.py`**: Tests for the function.

## Implementation Details
- **Function**: `find_repeated_elements(nums: list[int]) -> list[int]`
- **Algorithm**: Uses two sets: one to track seen elements, another for repeats.
- **Time Complexity**: O(n) where n is the list length (set operations are O(1)).
- **Space Complexity**: O(n) to store unique elements in sets.

