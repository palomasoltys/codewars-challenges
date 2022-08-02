# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in
# the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.
# In effect: 89 = 8^1 + 9^2
# The next number in having this property is 135.
# See this property again: 135 = 1^1 + 3^2 + 5^3
# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

# Let's see some cases:
# sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# sum_dig_pow(90, 100) == []

def sum_dig_pow(start, end):
    numbers = []

    for n in range(start, end+1):
        e = 1
        total = 0
        n = str(n)
        for i in n:
            total += int(i) ** e
            e += 1
        if total == int(n):
            numbers.append(int(n))
    return numbers


print(sum_dig_pow(1, 100))  # -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
print(sum_dig_pow(90, 100))  # -> []
