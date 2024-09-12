// https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&company=Amazon&sortBy=submissions
// Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.

// In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

/*
A **subarray** is a contiguous portion of an array. It consists of consecutive elements from the original array, meaning the elements in a subarray must occupy consecutive positions in the array and maintain their original order.

For example, consider the array:

`[1, 2, 3, 4]`

Possible subarrays include:

- `[1]`
- `[2, 3]`
- `[3, 4]`
- `[1, 2, 3, 4]`
  
However, non-contiguous selections like `[1, 3]` or `[2, 4]` are **not** subarrays.

Subarrays are often used in programming problems that involve searching for patterns or calculating sums, such as finding the maximum sum subarray (Kadane's Algorithm) or checking for specific conditions over certain ranges of the array.

To find a subarray whose sum is equal to a given number, you can use an efficient algorithm like the **sliding window** or **two-pointer** approach (for non-negative numbers). Here's how you can approach this:

### Sliding Window Approach (for non-negative numbers)

1. **Initialize two pointers**: `start` and `end` both set to the beginning of the array. These pointers will represent the boundaries of the current subarray.
2. **Initialize a variable `current_sum`**: This will store the sum of elements between `start` and `end`.
3. **Iterate through the array with `end`**: Expand the window by adding the element at the `end` pointer to `current_sum`.
4. **Check the sum**:
   - If `current_sum` is less than the target sum, move the `end` pointer to the right to include more elements.
   - If `current_sum` is greater than the target sum, move the `start` pointer to the right to exclude elements from the left side of the subarray.
   - If `current_sum` is equal to the target, you've found the subarray.
5. **Continue** until you find the subarray or exhaust the array.

### Code Example (in Python):

```python
def find_subarray_with_sum(arr, target_sum):
    start = 0
    current_sum = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        # Shrink the window as long as the current_sum is greater than target_sum
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
        
        # Check if we've found the target sum
        if current_sum == target_sum:
            return arr[start:end+1]
    
    return None  # Return None if no subarray is found
```

### Example:

```python
arr = [1, 3, 2, 5, 7, 2]
target_sum = 12
result = find_subarray_with_sum(arr, target_sum)
print(result)
```

**Output:**
```python
[5, 7]
```

### Time Complexity:
- The time complexity of this approach is **O(n)**, where `n` is the number of elements in the array. This is because each element is processed at most twice, once when adding to `current_sum` and once when subtracting from it.

### Note:
- This approach works well for **non-negative integers** because you can always shrink or expand the window as needed.
- For arrays with negative numbers, you would need to adjust the algorithm, possibly by using a **hashmap** to store sums and check for subarrays.



*/