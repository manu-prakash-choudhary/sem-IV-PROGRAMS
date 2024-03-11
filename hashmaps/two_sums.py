def two_sum(nums, target):
    # Create a dictionary to store the index of each number
    num_index_map = {}
    
    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement required to achieve the target
        complement = target - num
        
        # If the complement exists in the dictionary, return the indices
        if complement in num_index_map:
            return [num_index_map[complement], i]
        
        # Otherwise, store the current number's index in the dictionary
        num_index_map[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print("Indices of the two numbers:", two_sum(nums, target))
