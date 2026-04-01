# Valid Paretheses
def is_valid_parentheses(s):
    # Initialize a stack to keep track of opening parentheses
    stack = []
    # Create a mapping of closing parentheses to their corresponding opening parentheses
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    # Loop through each character in the string
    for char in s:
        if char in mapping:
            # If it's a closing parenthesis, check if the top element of the stack matches the corresponding opening parenthesis
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)
    
    return not stack

s = "([{}])"
print(is_valid_parentheses(s))