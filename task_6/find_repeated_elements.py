def find_repeated_elements(nums):
    seen = set()  # To store elements we've already seen
    repeated = set()  # To store elements that repeat

    for num in nums:
        if num in seen:  # If the number is already in the set, it's a repeat
            repeated.add(num)
        else:
            seen.add(num)  # Otherwise, add it to the seen set

    return repeated  # Return set directly