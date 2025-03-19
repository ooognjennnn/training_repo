# training_repo
Mine training repository
# Yes or No Task

This task implements a function to check for duplicates in a list.

## Overview
The `yes_or_no` function processes a list and prints "Yes" if an item has appeared before (duplicate) or "No" if it’s the first occurrence.

## Files
- **`yes_no_func.py`**: Contains the `yes_or_no` function implementation.

## Implementation Details
- **Function**: `yes_or_no(collection: list) -> None`
- **Algorithm**: Uses a `set` to track seen items.
- **Time Complexity**: O(n) where n is the length of the list (set operations are O(1) on average).
- **Space Complexity**: O(n) to store unique items in the set.
- **Behavior**: Prints "Yes" for duplicates, "No" for first occurrences.

## Example
```python
yes_or_no([1, 2, 3, 1, 2, 4, 2])