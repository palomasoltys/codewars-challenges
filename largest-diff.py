# Find the largest difference between integers in a sorted list
# [1, 5, 6, 7, 11] => 4
# [-11, -5, 0, 5, 11] => 6


def largest_diff_number(lst):
    lst.sort()
    largest = []
    for i in range(len(lst)-1):
        largest.append(lst[i+1] - lst[i])
    return max(largest)


print(largest_diff_number([1, 5, 6, 7, 11]))
print(largest_diff_number([-11, -5, 0, 5, 11]))
