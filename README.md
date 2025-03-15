# Factorial Calculation Task

This task implements three methods to calculate factorials: recursive, loop-based, and generator-based, along with tests.

## Overview
The goal is to compute factorials using different approaches and verify them with test cases. Each method is implemented in a separate file under `task_3/`.

## Files
- **`task_3/factorial_recursive_method.py`**: Recursive factorial implementation.
- **`task_3/factorial_loop_method.py`**: Iterative (loop-based) factorial implementation.
- **`task_3/factorial_generator_method.py`**: Generator-based factorial implementation.
- **`task_3/tests/test_factorial_recursive_method.py`**: Tests for the recursive method.
- **`task_3/tests/test_factorial_loop_method.py`**: Tests for the loop method.
- **`task_3/tests/test_factorial_generator_method.py`**: Tests for the generator method.
- **`.gitignore`**: Ignores compiled files like `.pyc` and `__pycache__`.

## Implementation Details
- **Recursive Method**: Uses function recursion to calculate n! (e.g., `n * factorial(n-1)`).
- **Loop Method**: Uses a loop to multiply numbers from 1 to n.
- **Generator Method**: Yields factorials incrementally using a generator.
- **Time Complexity**: O(n) for all methods (linear in terms of input n).
- **Space Complexity**: 
  - Recursive: O(n) due to call stack.
  - Loop: O(1) as it uses constant extra space.
  - Generator: O(1) per yield, O(n) if collecting all values.

## How to Run
1. Navigate to `task_3/`:
   ```bash
   cd task_3
