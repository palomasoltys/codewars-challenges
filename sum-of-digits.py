# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced.
# The input will be a non-negative integer.

#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(num):

    num = str(num)

    if len(num) == 1:
        return int(num)

    while len(num) > 1:
        soma = 0
        for i in range(len(num)):
            soma += int(num[i])
        num = str(soma)
    return soma


print(digital_root(132189))  # -> 6
print(digital_root(493193))  # -> 2
