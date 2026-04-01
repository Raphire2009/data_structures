# Reversed string using slicing
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))



# valid palindrome
# Two pointers approach
def is_palindrome(s):
    # Initialize two pointers, one at the beginning and one at the end of the string
    left, right = 0, len(s) - 1
    # Loop until the two pointers meet
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        # Compare the characters at the left and right pointers, ignoring case
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
        
    return True

print(is_palindrome("madam"))