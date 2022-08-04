# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
# Example:
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):

    new_string = ''
    for i in range(len(s)):
        if s[i] == 'a':
            new_string += 'b'
        elif s[i] == 'b':
            new_string += 'a'
        else:
            new_string += s[i]
    return new_string


print(switcheroo('acb'))
print(switcheroo('aabacbaa'))
