# Bubble Sort Task

This branch contains a simple implementation of the Bubble Sort algorithm as part of a training task.

## Overview
The purpose of this task was to implement a Bubble Sort algorithm in Python and provide test cases to verify its correctness. The code is organized in the `task_2/` directory.

## Files
- **`task_2/bubble_sort.py`**: Contains the Bubble Sort implementation.
- **`task_2/tests/test_bubble_sort.py`**: Contains test cases to validate the sorting algorithm.
- **`.gitignore`**: Ensures temporary files like `__pycache__` and `.pyc` are not tracked.

## Implementation Details
- **Algorithm**: Bubble Sort
- **Time Complexity**: 
  - Worst case: O(n²) — Input list is arranged in descending order.
  - Best case: O(n) — With early exit optimization (if implemented).
  - Average case: O(n²).
- **Space Complexity**: O(1) (in-place sorting).
- **Features**:
  - Sorts the input list in ascending order using adjacent element comparisons.
  - Modifies the input list directly (in-place).

## How to Run
To run and test the sorting algorithm, follow these steps:

1. Navigate to the project root directory (from your terminal).

2. Run the tests to validate the implementation:
   ```bash
   pytest