def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    import math

    perfect_square = (math.sqrt(sq) // 1) * (math.sqrt(sq) // 1) == sq

    if not perfect_square:
        return -1
    else:
        return (math.sqrt(sq) + 1) ** 2


print(find_next_square(100))
print(find_next_square(99))
