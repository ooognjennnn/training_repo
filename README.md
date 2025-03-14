# training_repo
### Task 1: yes_or_no Function
- **Description**: Implemented the `yes_or_no` function to check for duplicate elements in a list.
- **Status**: Completed ✅
- **Details**:
  - The function iterates through the input list and prints `"Yes"` if an element has already been seen, or `"No"` if it's the first occurrence.
  - Example usage:
    ```python

    input_list = [1, 2, 3, 1, 2, 4, 2]
    yes_or_no(input_list)
    ```
  - Expected Output:
    ```
    No
    No
    No
    Yes
    Yes
    No
    Yes
    ```
#  Task -3 Factorial Calculation Implementations

This project contains three different implementations of factorial calculation (`n!`) in Python, as per the task requirements. Each method takes an integer `n` and returns its factorial (`n!`).

## Features
- **Recursive**: Uses recursive function calls to compute `n!`.
- **Loop**: Uses an iterative approach with a for loop.
- **Generator**: Uses a generator to yield intermediate results.

All implementations:
- Print a message for negative numbers: "Factorial is not defined for negative numbers".
- Return `1` for `n = 0` (since `0! = 1`).
- Are tested with examples like `n = 5` (returns `120`) and `n = 0` (returns `1`).

## Usage
Run the Python script and call any of the functions with `n = 5`. All methods return the same result:
Recursive: 120
Loop: 120
Generator: 120


## Implementation Details
1. **Recursive Method (`factorial_recursive`)**  
   - Uses recursion: `n! = n * (n-1)!`.
   - Base cases: `0! = 1`, `1! = 1`.

2. **Loop Method (`factorial_loop`)**  
   - Iterates from 1 to `n`, multiplying each number into a result.
   - Efficient for larger numbers (no recursion depth limit).

3. **Generator Method (`factorial_generator`)**  
   - Yields intermediate factorial results (e.g., `1, 2, 6, 24, 120` for `n=5`).
   - Final `n!` is extracted from the last yielded value.

## Code Example
```python
# Example usage
print(factorial_recursive(5))  # 120
print(factorial_loop(5))       # 120
print(factorial_generator(5))  # 120
