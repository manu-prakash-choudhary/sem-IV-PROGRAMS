import heapq

def product_of_three_largest(nums):
    # Create a max heap
    max_heap = []
    
    # Add all elements to the max heap
    for num in nums:
        heapq.heappush(max_heap, -num)  # Negate the numbers to create a max heap
        
    # Remove duplicates
    distinct_nums = set(nums)
    
    # Pop the three largest distinct elements from the max heap
    largest_elements = set()
    while len(largest_elements) < 3:
        num = -heapq.heappop(max_heap)  
        largest_elements.add(num)

        
    
    # Calculate the product of the three largest distinct elements
    product = 1
    for num in largest_elements:
        product *= num
    
    return product


nums = [1, 5, 2, 6, 9, 4, 9, 10]
print("Product of the three largest distinct elements:", product_of_three_largest(nums))
