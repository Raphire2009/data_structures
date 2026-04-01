# Hash Table
# Contains duplicate

def contains_duplicate(nums):
    # Create a set to store seen numbers
    seen = set()
    # Loop through each number in the list
    for num in nums:
        # If the number is already in the set, we have a duplicate
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)
    return False

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))

# Two Sum
def two_sum(nums, target):
    # Create a hash map to store the indices of the numbers
    hash_map = {}
    # Loop through the list of numbers
    for i, num in enumerate(nums):
        complement = target - num
        # Check if the complement exists in the hash map
        if complement in hash_map:
            return [hash_map[complement], i]
        # Otherwise, add the current number and its index to the hash map
        hash_map[num] = i
    return []

nums = [2, 7, 11, 15]
target = 13  
print(two_sum(nums, target))    