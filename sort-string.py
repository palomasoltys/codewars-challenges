def alphabetic(s):
    print(s)
    s_sorted = sorted(s)
    print(s_sorted)
    return s == "".join(s_sorted)


print(alphabetic('door'))
print(alphabetic('cell'))
