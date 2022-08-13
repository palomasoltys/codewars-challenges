# You are to write an function that takes a string as it's first paramter. This string will be a string of words.
# You are expected to then use the second parameter, which will be an integer, to find the corresponding word in the given string. The first word would be represented by 0.
# Once you have the located string you are finally going to multiply by it the third provided paramater, which will also be an interger. You are additionally required to add a hyphen in between each word.


def modify_multiply(st, loc, num):
    st = st.split()
    st_lst = []
    for _ in range(num):
        st_lst.append(st[loc])
    return "-".join(st_lst)


# -> "string-string-string-string-string"
print(modify_multiply("This is a string", 3, 5))
