# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

def valid_braces(string):
    braces = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if stack and braces.get(char) == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return False
    else:
        return True


print(valid_braces("(){}[]"))  # -> True
print(valid_braces("[(])"))  # -> False
