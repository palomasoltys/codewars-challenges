# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language)
# like so: (index1, index2).

# The input will always be valid (numbers will be an array of length 2 or greater,
# and all of the items will be numbers; target will always be the sum of two different items from that array).

# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]

def two_sum(numbers, target):

    index = []

    for i_index, i in enumerate(numbers):  # 1 / #2 / #3
        for j_index, j in enumerate(numbers):  # 1 2 3 / #1 2 3 / #1 2 3
            if j_index > 0:
                if i + j == target:
                    index.append(i_index)
                    index.append(j_index)
                    break

    return index[:2]


# print(two_sum([1, 2, 3], 4))  # -> [0,2]
# print(two_sum([2, 2, 3], 4))  # ->[0,1]
# print(two_sum([1234, 5678, 9012], 14690))  # -> [1,2]


def two_sum_optimized(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        num_to_sum = target - nums[i]
        if num_to_sum in hashmap:
            return [hashmap[num_to_sum], i]
        hashmap[nums[i]] = hashmap.get(nums[i], i)


print(two_sum_optimized([2, 7, 11, 15], 9))  # -> [0,1]
