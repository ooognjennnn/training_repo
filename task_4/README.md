# Fibonacci Calculation Task

This task implements three methods to calculate Fibonacci numbers: recursive, loop-based, and generator-based, along with tests.

## Overview
The goal is to compute Fibonacci numbers using different approaches and verify them with test cases. Each method is implemented in a separate file under `task_4/`.

## Files
- **`task_4/fibonacci_recursive_method.py`**: Recursive Fibonacci implementation.
- **`task_4/fibonacci_loop_method.py`**: Iterative (loop-based) Fibonacci implementation.
- **`task_4/fibonacci_generator_method.py`**: Generator-based Fibonacci implementation.
- **`task_4/tests/test_fibonacci_recursive_method.py`**: Tests for the recursive method.
- **`task_4/tests/test_fibonacci_loop_method.py`**: Tests for the loop method.
- **`task_4/tests/test_fibonacci_generator_method.py`**: Tests for the generator method.
- **`.gitignore`**: Ignores compiled files like `.pyc` and `__pycache__`.

## Implementation Details
- **Recursive Method**: Calculates Fibonacci(n) recursively (e.g., `fib(n-1) + fib(n-2)`).
- **Loop Method**: Uses a loop to iteratively compute Fibonacci numbers.
- **Generator Method**: Yields Fibonacci numbers incrementally using a generator.
- **Time Complexity**:
  - Recursive: O(2^n) due to exponential recursive calls.
  - Loop: O(n) as it iterates linearly.
  - Generator: O(n) to generate n numbers.
- **Space Complexity**:
  - Recursive: O(n) due to call stack.
  - Loop: O(1) as it uses constant extra space.
  - Generator: O(1) per yield.

