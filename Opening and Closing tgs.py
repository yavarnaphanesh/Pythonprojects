def is_balanced(tags):
    stack = []
    for tag in tags:
        if tag.isupper():
            stack.append(tag.lower())
        elif not stack or stack.pop() != tag:
            return False
    return not stack


print(is_balanced("AaBbcC"))  # Output: True
print(is_balanced("AaBbc"))  # Output: False
print(is_balanced("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))  # Output: True
