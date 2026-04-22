""" check if paired """
def is_paired(input_string):
    """Check if brackets are properly nested and paired."""
    pairs = {")": "(", "]": "[", "}": "{"}
    # Pre-defining the set of opening brackets for speed
    openers = set(pairs.values())
    stack = []

    for char in input_string:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            # If stack is empty or the top doesn't match the required opener
            if not stack or stack.pop() != pairs[char]:
                return False
                
    return not stack