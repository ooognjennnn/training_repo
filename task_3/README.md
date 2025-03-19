# Factorial Calculation Task

This task implements three methods to calculate factorials: recursive, loop-based, and generator-based, along with tests.

## Overview
The goal is to compute factorials using different approaches and verify their functionality with test cases. Each method is implemented in a separate file under the `task_3/` directory.

## Files
- **`task_3/factorial_recursive_method.py`**: Recursive factorial implementation.
- **`task_3/factorial_loop_method.py`**: Iterative (loop-based) factorial implementation.
- **`task_3/factorial_generator_method.py`**: Generator-based factorial implementation.
- **`task_3/tests/test_factorial_recursive_method.py`**: Tests for the recursive method.
- **`task_3/tests/test_factorial_loop_method.py`**: Tests for the loop-based method.
- **`task_3/tests/test_factorial_generator_method.py`**: Tests for the generator-based method.
- **`.gitignore`**: Ensures temporary files such as `.pyc` and `__pycache__` are not tracked by Git.

## Implementation Details
### Methods
1. **Recursive Method**: 
   - Implements a recursive formula to calculate factorial:  
     `factorial_recursive(n) = n * factorial_recursive(n-1)`  
   - Automatically handles the base case for `n = 0 or 1`.

2. **Loop Method**:
   - Uses an iterative loop to multiply numbers from `1` to `n`.

3. **Generator Method**:
   - Yields factorial values incrementally, making it memory-efficient when only specific factorials are needed.

### Complexity Analysis
- **Time Complexity**: O(n) for all methods — the computation scales linearly with `n`.  
- **Space Complexity**:
  1. Recursive: O(n) due to recursive calls stored on the call stack.
  2. Loop: O(1) as it uses constant extra space.
  3. Generator: O(1) memory for each yield, O(n) if collecting all factorials into memory.

## How to Run
### Running the Code
You can run and test each implementation individually by importing the methods into a Python script or interactive Python session.

Example:
```python
from task_3.factorial_recursive_method import factorial_recursive
from task_3.factorial_loop_method import factorial_loop
from task_3.factorial_generator_method import factorial_generator

# Recursive method
print(factorial_recursive(5))  # Output: 120

# Loop method
print(factorial_loop(5))  # Output: 120

# Generator method
gen = factorial_generator(5)
for val in gen:
    print(val)  # Output: 1, 2, 6, 24, 120