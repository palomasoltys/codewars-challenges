# In this kata, you have an input string and you should check whether it is a valid message. To decide that, you need to split the string by the numbers, and then compare the numbers with the number of characters in the following substring.

# For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2, hi and the function should return true, because "hey" is 3 characters, "hello" is 5, and "hi" is 2; as the numbers and the character counts match, the result is true.

# "4code13hellocodewars" -> True
# "3hey5hello2hi" -> True
# "hello5" -> False
# "" -> True

import re


def is_a_valid_message(message):

    if message == "":
        return True
    if message[0].isalpha() or message[len(message) - 1].isdigit():
        return False

    string = re.findall('[a-zA-Z]+', message)
    num = re.findall('[0-9]+', message)

    if len(num) != len(string):
        return False

    for i in range(len(string)):
        if len(string[i]) != int(num[i]):
            return False

    return True


print(is_a_valid_message("3hey5hello2hi"))  # -> True
print(is_a_valid_message("4code13hellocodewars"))  # -> True
print(is_a_valid_message("hello5"))  # -> False
print(is_a_valid_message(""))  # -> True
